class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Config(Singleton):
    def __init__(self,config_json=None):
        if not hasattr(self, 'config'):
            self.config = config_json

    def get_products(self) -> list[str]:
        return self.config.get("products", [])

    def get_camera_config(self) -> dict:
        return self.config.get("camera", {})
