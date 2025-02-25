import queue

from PySide6.QtWidgets import QWidget, QLabel
from attr import dataclass

from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult
from src.IHM.src.components.history.history_ui import Ui_Form
@dataclass
class Logs:
    hist: QWidget
    position:QLabel
    result: QLabel

    def set_result(self,result:str):
        self.result.setText(result)

    def set_position(self,position:str):
        self.position.setText(position)

    def setStyleSheet(self,style:str):
        self.hist.setStyleSheet(style)

class History(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super(History,self).__init__(parent)
        self.queue_history = None
        self.setupUi(self)
        self._config_logs()


    def _config_logs(self):
        if self.queue_history is None:
            self.queue_history = queue.Queue()
        self.queue_history.put(Logs(self.hist_one,self.hist_one.children()[1],self.hist_one.children()[2]))
        self.queue_history.put(Logs(self.hist_two,self.hist_two.children()[1],self.hist_two.children()[2]))

    def receive_result(self, position: str, result: InspectionResult):
        if self.is_history_full():
            self.clean_history()

        log: Logs = self.queue_history.get()
        log.set_position(position)
        if result == InspectionResult.APROVADO:
            log.set_result('APROVADO')
            log.setStyleSheet("background-color: #00A336; color: white;")


        elif result == InspectionResult.REPROVADO:
            log.set_result('REPROVADO')
            log.setStyleSheet("background-color: #ff0000; color: white;")

        self.queue_history.put(log)  # Coloca o objeto de volta na fila

    def clean_history(self):
        for _ in range(0, self.queue_history.qsize()):
            log: Logs = self.queue_history.get()
            log.set_position("")
            log.set_result("INSPECIONANDO...")
            log.setStyleSheet("background-color: yellow")
        self._config_logs()

    def is_history_full(self) -> bool:
        if self.result.text() != "INSPECIONANDO..." and self.result_2.text() != "INSPECIONANDO...":
            return True
        return False
