import socket
import threading
import time
from config import HOST, PORT, CADEIRAS

fila_espera = []
lock = threading.Lock()
barbeiro_dormindo = True


def atender_clientes():
    global barbeiro_dormindo

    while True:
        if fila_espera:
            with lock:
                cliente_conn = fila_espera.pop(0)

            print("💈 Atendendo cliente...")
            time.sleep(3)

            cliente_conn.sendall("CORTADO\n".encode())
            cliente_conn.close()

            print("📢 PRÓXIMO")
        else:
            if not barbeiro_dormindo:
                print("😴 Barbeiro dormindo...")
                barbeiro_dormindo = True
            time.sleep(2)


def lidar_cliente(conn, addr):
    global barbeiro_dormindo

    print(f"👤 Cliente chegou: {addr}")

    with lock:
        if len(fila_espera) < CADEIRAS:
            fila_espera.append(conn)
            print(f"🪑 Cliente aguardando. Fila: {len(fila_espera)}")

            if barbeiro_dormindo:
                print("🔊 ACORDA! Hora de trabalhar!")
                barbeiro_dormindo = False

        else:
            print("❌ Barbearia cheia. Cliente foi embora.")
            conn.sendall("CHEIA\n".encode())
            conn.close()


def iniciar_servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"🚀 Barbearia aberta em {HOST}:{PORT}")

    threading.Thread(target=atender_clientes, daemon=True).start()

    while True:
        conn, addr = server.accept()
        threading.Thread(target=lidar_cliente, args=(conn, addr)).start()


if __name__ == "__main__":
    iniciar_servidor()