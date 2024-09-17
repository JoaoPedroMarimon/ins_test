from src.IHM.src.components.communication.Enum.Inspection_order import InspectionOrder


class ControllerOrder:
    def __init__(self):
        self._list_functions: dict = {}

    def add_funcion(self, func, enum_key: InspectionOrder):
        self._list_functions[enum_key] = func

    def get_all_func(self) -> dict:
        return self._list_functions

    def get_func(self,enum_key):
        return self._list_functions.get(enum_key)
