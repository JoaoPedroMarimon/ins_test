import sys

from PySide6.QtCore import QObject, Signal
from PySide6.QtNetwork import QLocalServer, QHostAddress, QTcpServer, QLocalSocket

from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult
from src.IHM.src.components.communication.Enum.Inspection_order import InspectionOrder
from src.IHM.src.components.communication.message_controller import  MessageController
from src.IHM.src.components.communication.controller_order import ControllerOrder

class IHMServer(QObject):
    OnReceiveResult = Signal(InspectionResult)

    def __init__(self, controller_order: ControllerOrder = None):
        super().__init__()
        self._controller_order = controller_order if controller_order is not None else ControllerOrder()
        self.__configuranting_server()

    def __configuranting_server(self):
        system = sys.platform
        if system == "linux":
            self._server = QLocalServer(self)
            self._server.removeServer("/tmp/IHM")
            self._server.listen("/tmp/IHM")
        else:
            self._address = QHostAddress()
            self._address.setAddress("127.0.0.1")
            self._server = QTcpServer(self)
            self._server.listen(self._address, 1111)

        self._server.newConnection.connect(self.__on_new_connection)

    def __on_new_connection(self):
        self._client: QLocalSocket = self._server.nextPendingConnection()
        self._client and self._client.readyRead.connect(self.handle_request)
        self._client.disconnected.connect(self.__on_client_disconnected)

    def __on_client_disconnected(self):
        print("Client disconnected")
        self._client.deleteLater()
        self._client = None

    def handle_request(self):
        req = self._client.readAll()
        result = MessageController.convert_to_enum(req)
        #dividir entre reagir uma informação e dar uma informação
        match result:
            case result if result in InspectionResult:
                self.OnReceiveResult.emit(result)
            case result if result in InspectionOrder:
                function = self._controller_order.get_func(result)
                response = function()
                self._client.write(bytes(response,"utf-8"))

    def add_order_functions(self, functions, enum_key: InspectionOrder | InspectionResult):
        match enum_key:
            case enum_key if enum_key in InspectionOrder:
                self._controller_order.add_funcion(functions, enum_key)
            case enum_key if enum_key in InspectionResult:
                self.OnReceiveResult.connect(functions)

    def close(self):
        self._server.close()
        self._client.close()
