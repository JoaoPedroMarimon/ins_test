import queue
import time
from zipfile import error


class Arduino:
    '''
    This class simulate what arduino does

    step -1 = dont execute nothing

    step 0 = send to main about the new cycle

    step 1 = discard or not the switches (dont need this code in this class)

    step 2 and 3 = send when the switch need to be inspected
    '''
    def __init__(self):
        self.teste = None
        self.in_buffer = queue.Queue()
        self.out_buffer = queue.Queue()
        self.error_counter = 0
        self._step = -1

    def write(self, message: bytes) -> None:
        self.in_buffer.put(message)
        self.simulate()

    @property
    def in_waiting(self) -> int:
        return self.out_buffer.qsize()

    def read_line(self) -> bytes:
        if self.in_waiting > 0:
            return self.out_buffer.get()
        return b""

    def _waiting_serial(self) -> bool:
        while self.in_buffer.qsize() == 0:
            time.sleep(0.1)
        return True


    def simulate(self):
        if self.in_buffer.qsize() == 0:
            entry = None
        else:
            entry = self.in_buffer.get()
        if entry is not None:
            match entry: #mensages from main
                case b'y':
                    print("Fecho ciclo")
                    self._step = -1

                case b'x':
                    print("inicio inspeção")
                    self._step = 2

                case b'o':
                    print("placa sem defeito")

                case b'n':
                    print("placa com defeito")
                    self.error_counter += 1
        time.sleep(3)
        #mesages to main!
        if self.error_counter > 6:
            self.out_buffer.put(b"w")
        else:
            match self._step:
                case 0:
                    self.out_buffer.put(b'k')
                    time.sleep(3)
                    self._step = 2
                    self.simulate()
                case 2:
                    self.out_buffer.put(b'p')
                    self._step = 3
                case 3:
                    self.out_buffer.put(b's')
                    self._step = 0

