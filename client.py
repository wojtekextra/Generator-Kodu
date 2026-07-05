import socket
from generated_code import UserData

def start_client():
    host = '127.0.0.1'
    port = 65432

    # Tworzenie obiektu danych
    user = UserData(67, "WojciechCybulski")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        # Serializacja za pomocą metody wygenerowanej w kodzie
        binary_data = user.serialize()
        s.sendall(binary_data)
        print("Dane zostały wysłane do serwera.")

if __name__ == "__main__":
    start_client()