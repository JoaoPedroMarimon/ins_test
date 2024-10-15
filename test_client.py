import socket
import time

def run_client():
    client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client_socket.connect("/tmp/IHM")

    # Enviar pacotes
    for i in range(5):
        data = f"Mensagem {i+1}".encode('utf-8')
        packet_length = len(data)
        client_socket.sendall(packet_length.to_bytes(4, byteorder='big'))
        client_socket.sendall(data)
        time.sleep(1)

    client_socket.close()

if __name__ == "__main__":
    run_client()
