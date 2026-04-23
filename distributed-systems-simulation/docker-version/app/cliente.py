import socket
import time
import random
from config import SERVER_HOST, PORT


def cliente(id):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_HOST, PORT))

        print(f"👤 Cliente {id} entrou na barbearia")

        resposta = s.recv(1024).decode()

        if resposta.strip() == "CHEIA":
            print(f"❌ Cliente {id} foi embora (lotado)")
        else:
            print(f"💇 Cliente {id} foi atendido")

        s.close()

    except Exception as e:
        print(f"Erro cliente {id}: {e}")


if __name__ == "__main__":
    i = 1
    while True:
        cliente(i)
        i += 1
        time.sleep(random.uniform(0.5, 2))