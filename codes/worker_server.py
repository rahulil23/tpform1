import socket
import threading

def worker_server(server_id):
    port = 8080 + server_id
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen(5)
    print(f"Worker server {server_id} listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        message = client_socket.recv(1024).decode()
        
        # Menentukan jenis aplikasi (Long/Short) dari pesan
        app_id, app_type = message.split(":")
        if app_type == "Long":
            response = f"Worker {server_id} processed complex (Long) request for {app_id}."
        else:
            response = f"Worker {server_id} processed simple (Short) request for {app_id}."
        
        client_socket.send(response.encode())
        client_socket.close()

# Memulai tiga worker server pada port 8081, 8082, dan 8083
for i in range(1, 4):  # server_id = 1, 2, 3 -> port 8081, 8082, 8083
    threading.Thread(target=worker_server, args=(i,)).start()
