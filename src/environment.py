import os

def get_env_ensured(key: str) -> str:
    """
    Ensures the environment variable exists.
    """
    value = os.getenv(key)
    if not value:
        msg = f"Variável de ambiente '{key}' indefinida."
        raise EnvironmentError(msg)
    return value

DEFAULT_CONFIGFILE = {
    "camera": {"server": "192.168.1.108",
               "login": "admin",
               "password": "admin123",
               "rtsp_port": "554"},
    "products": []
}

PAD_INSPECT_TIMEOUT = 5.8

CONFIGFILE_PATHNAME = "./conf.json"
