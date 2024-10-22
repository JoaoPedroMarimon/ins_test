import queue

from src.IHM.hmi_receiver import HMIReceiver

servidor = HMIReceiver()

while True:
        try:
            packet = servidor._packet_queue.get(timeout=1)
            print(f"Pacote recebido: {packet}")
        except queue.Empty:
            continue