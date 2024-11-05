import logging
import argparse
import re
from argparse import ArgumentParser

from main_inspecao import inspecionar_frame
from .serial_connection import SerialController
from . import environment as env
from . import utils
from .inspection_designer.inspection_designer import inspection


class NotAProductError(Exception):
    def __init__(self, code: str | None, name: str | None):
        message = f"O produto com identificação '{code if code else name}' não existe."
        super().__init__(message)


def alphanumeric(value):
    if not re.match("^[a-zA-Z0-9]+$", value):
        raise argparse.ArgumentTypeError("Only alphanumeric characters are allowed.")
    return value


def main_parse():
    parser = ArgumentParser()
    parser.add_argument("--debug", action="store_true",
                        help="Mostra diversas informações do que está acontecendo durante a execução do programa.")

    group = parser.add_mutually_exclusive_group()

    group.add_argument("-sp", "--serial-port", type=str, metavar="port",
                       help="Determina a porta serial do microcontrolador.")

    group.add_argument("-ns", "--no-serial", action="store_true",
                       help="Ignora a conexão serial, realizando os testes com um trigger pelo prompt.")

    parser.add_argument("-ws", "--write-serial", nargs="+", dest="serial_data", metavar='bytes',
                        type=alphanumeric)

    parser.add_argument("-ndbc", "--no-database-commit", action="store_true",
                        help="Não envia dados de teste para o banco de dados MySQL.")

    parser.add_argument("--no-pad-inspection", action="store_false", dest="pad_inspec_active",
                        help="Ignora o teste de inspeção visual da tampografia do produto.")

    parser.add_argument('--no-perf-test', action="store_false", dest="perf_test_active",
                        help="Ignora o teste de performance do produto.")

    parser.add_argument("--no-led-inspection", action="store_false", dest="led_inspec_active",
                        help="Ignora o teste de inspeção visual dos LEDS do produto.")

    subparser = parser.add_subparsers(dest="subparser")

    add_parser = subparser.add_parser("add", help="Adiciona um novo produto no arquivo.")
    add_parser.add_argument("name", type=str, help="Nome do produto, sem caracteres especiais.")
    add_parser.add_argument("code", type=str, help="Código do produto.")
    add_parser.add_argument("status", type=str, help="Status da inspecao.")

    edit_parser = subparser.add_parser("edit", help="Edita um produto existente no arquivo.")
    group = edit_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-n", "--name", type=str, help="Nome de um produto existente no arquivo.")
    group.add_argument("-c", "--code", type=str, help="Código de um produto existente no arquivo.")
    group.add_argument("-s", "--status", type=str, help="Status da inspecao.")

    del_parser = subparser.add_parser("del", help='Apaga um produto existente do arquivo, além de suas pastas.')
    group = del_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-n", "--name", type=str, help="Nome de um produto existente no arquivo.")
    group.add_argument("-c", "--code", type=str, help="Código de um produto existente no arquivo.")

    inspect_parser = subparser.add_parser("inspect", help="Abre a interface de inspeção visual para "
                                                          "um produto existente.")
    group = inspect_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-n", "--name", type=str, help="Nome de um produto existente no arquivo.")
    group.add_argument("-c", "--code", type=str, help="Código de um produto existente no arquivo.")

    inspect_parser.add_argument("inspection", choices=("pad-inspection", "led-inspection"),
                                help="Tipo de inspeção visual a ser utilizada.")

    clone_parser = subparser.add_parser("clone", help="Clona as configurações de um produto alvo "
                                                      "para um produto destino.")

    group = clone_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-tn", "--target-name", type=str,
                       help="Nome do produto alvo existente no arquivo.")
    group.add_argument("-tc", "--target-code", type=str,
                       help="Código do produto alvo existente no arquivo.")

    group = clone_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-dn", "--dest-name", type=str,
                       help="Nome do produto destino existente no arquivo.")
    group.add_argument("-dc", "--dest-code", type=str,
                       help="Código do produto destino existente no arquivo.")

    group = clone_parser.add_argument_group()
    group.add_argument("-pic", "--pad-inspection-config", action="store_true",
                       help="Clona as configurações da inspeção de tampografia")
    return parser.parse_args()


def execute_parse(args) -> None:
    config = utils.load_json_configfile(env.CONFIGFILE_PATHNAME, default=env.DEFAULT_CONFIGFILE)

    if args.serial_data:
        port: str = utils.get_port_connection()
        if not port and not args.no_serial and not args.serial_port:
            msg = f"Não foi possível encontrar a porta do Arduino, portas listadas: {utils.get_all_ports()}"
            raise ConnectionError(msg)
        port = args.serial_port if args.serial_port else port

        with SerialController(port, False, args.debug) as ser:
            ser.ensure_step_zero()
            for data in args.serial_data:
                logging.debug(f"Serial W bytes b'{data}'")
                ser.write(data.encode("utf-8"))

    if args.subparser == "add":
        product_data = {"name": args.name.upper().replace(" ", ""),
                        "code": args.code,
                        "status": args.status.upper().replace(" ", ""),
                        "pad-inspection": {"active": True, "classes": []}}

        config["products"].append(product_data)
        config["products"] = sorted(config["products"], key=lambda x: int(x["code"]))
        utils.dump_json_configfile(env.CONFIGFILE_PATHNAME, config)
        logging.warning(f"|ADD| Produto '{product_data['name']}' adicionado à lista de produtos.")

    elif args.subparser == "edit":
        product_data = get_product_from_configfile(args.code, args.name, config)

    elif args.subparser == "del":
        product_data = get_product_from_configfile(args.code, args.name, config)

        config["products"].remove(product_data)
        config["products"] = sorted(config["products"], key=lambda x: x["code"])
        utils.dump_json_configfile(env.CONFIGFILE_PATHNAME, config)
        logging.warning(f"|DEL| Produto '{product_data['name']}' removido da lista de produtos.")

    elif args.subparser == "inspect":
        product_data = get_product_from_configfile(args.code, args.name, config)

        if args.inspection == "pad-inspection":
            inspection_obj = inspection.TemplateInspection(templates_path=f"./samples/{product_data['name']}/templates")

            inspection_obj.config = product_data[args.inspection]
            window = inspection_obj.load_designer(product_data['name'])
      #      window.load_video_source(utils.get_rtsp_url(**config["camera"]))
            do_save = window.mainloop()
            if do_save:
                utils.dump_json_configfile(env.CONFIGFILE_PATHNAME, config)
                logging.warning(f"|INSPECT| Produto '{product_data['name']}' teve inspeções"
                                f" do tipo {args.inspection} atualizadas.")

    elif args.subparser == "clone":
        target_product_data = get_product_from_configfile(args.target_code, args.target_name, config)
        dest_product_data = get_product_from_configfile(args.dest_code, args.dest_name, config)

        # it clones only when -lic and/or -pic are specified
        if args.led_inspection_config or args.pad_inspection_config:
            if args.pad_inspection_config:
                dest_product_data["pad-inspection"] = target_product_data["pad-inspection"]

            utils.dump_json_configfile(env.CONFIGFILE_PATHNAME, config)
            logging.warning(f"|CLONE| Configurações do produto '{target_product_data['name']}' adicionadas ao "
                            f"produto '{dest_product_data['name']}'.")


def get_product_from_configfile(code: str, name: str, config: dict) -> dict:
    """
    Gets a product dict object based on the `code` or `name` parameter from `config` parameter.
    """
    if code:
        key_search = "code"
        value_search = code
    else:
        key_search = "name"
        value_search = name
    for product in config["products"]:
        if product[key_search] == value_search:
            return product
    raise NotAProductError(code, name)
