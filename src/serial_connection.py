import serial
import logging

class PortLockedError(Exception):
    pass

class SerialConnection(serial.Serial):
    def __init__(self, port, no_serial=False, debug=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._no_serial = no_serial
        self._debug = debug
        self._lock_file = None

        if not self._no_serial:
            self.setPort(port)
            self.open()
            self._acquire_lock()

    def _acquire_lock(self) -> None:
        if self.isOpen():
            logging.debug('Serial acquire port lock')
            self._lock_file = open(self.port, 'wb')

    def _release_lock(self) -> None:
        if self._lock_file:
            logging.debug('Serial release port lock')
            self._lock_file.close()
            self._lock_file = None

    @staticmethod
    def _no_serial_prompt() -> bytes:
        prompt = input("NO-SERIAL: ")
        return prompt.encode()

    def cleanup(self) -> None:
        """
        Tenta enviar um sinal de REINICIAR LOOP para a Serial antes de encerrar o programa.
        """
        if not self._no_serial:
            logging.debug('Serial cleanup')
            self._release_lock()
            self.close()

    def readline(self, __size=None) -> bytes:
        if not self.isOpen():
            return self._no_serial_prompt()
        line = super().readline(__size)
        logging.debug(f"reading line {repr(line)} from serial")
        return line

    def read(self, size=1):
        if not self.isOpen():
            return self._no_serial_prompt()
        read = super().read(size)
        logging.debug(f"reading byte {repr(read)} from serial")
        return read

    def __enter__(self):
        if self._port is not None and not self.is_open:
            self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

    def inWaiting(self):
        if self._no_serial:
            return True
        return super().inWaiting()


class SerialController(SerialConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def approved(self) -> None:
        """
        Envia um sinal de APROVADO para a serial valor bytes b'a' caso a porta serial esteja aberta.
        """
        if self.isOpen():
            logging.debug("Serial W approved b'a'")
            self.write(b'a')

    def reproved(self) -> None:
        """
        Envia um sinal de REPROVADO para a serial valor bytes b'r' caso a porta serial esteja aberta.
        """
        if self.isOpen():
            logging.debug("Serial W reproved b'r'")
            self.write(b'r')

    def ensure_step_zero(self) -> None:
        """
        Envia um sinal de REINICIAR LOOP para serial valor bytes b's' caso a porta serial esteja aberta.

        Garante que o código do microcontrolador não fique preso esperando algo que nunca virá.
        """
        if self.isOpen():
            logging.debug("Serial W ensure_step_zero b's'")
            self.write(b's')

    def product_available(self):
        """
        Verifica se na serial há o valor em bytes b'i' (vinda do microcontrolador),
        isso significa que a gaveta foi fechada.
        """
        return self.readline().strip(b'\r\n') == b'i'

    def connect_rj45(self):
        if self.isOpen():
            logging.debug("Serial W connect_rj45 b'f'")
            self.write(b'f')

    def product_disconnected(self) -> bool:
        """
        Verifica se na serial há o valor em bytes b's' (vinda do microcontrolador), retorna True
        se a condição for verdadeira, caso contrário retorna False. Não trava a execução (non-blocking code).

        Este sinal é recebido quando o produto é desconectado pelas válvulas pressionando o botão.
        """
        while self.inWaiting():
            read = self.readline().strip(b'\r\n')
            if read == b"s":
                return True
        return False
    
    