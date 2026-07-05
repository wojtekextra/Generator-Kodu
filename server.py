import socket
from generated_code import UserData

def start_server():
    host = '127.0.0.1'
    port = 65432

    # Tworzenie gniazda
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Serwer nasłuchuje na {host}:{port}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Połączono z {addr}")
            data = conn.recv(1024) # Odbiór danych binarnych
            if data:
                # Deserializacja za pomocą metody wygenerowanej w kodzie
                user = UserData.deserialize(data)
                print(f"Otrzymano dane: ID={user.id}, Username={user.username}")

if __name__ == "__main__":
    start_server()