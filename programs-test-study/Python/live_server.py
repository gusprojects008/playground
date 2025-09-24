import socket
import threading

path = "./index.html"

def socket_server(path):
    def client_connection(client, path):
        try:
           client_request = client.recv(1024).decode("utf-8")
           if not client_request:
              return #"Waiting client connection..."
           print(client_request)

           with open(path, "rb") as file:
                file_content = file.read()
                response = (
                   "HTTP/1.1 200 OK\r\n"
                   "Content-Type: text/html\r\n"
                   f"Content-Length: {len(file_content)}\r\n"
                   "Connection: close\r\n"
                   "\r\n"
                ).encode("utf-8") + file_content
                client.sendall(response)
        except FileNotFoundError as error:
               response = (
                  "HTTP/1.1 404 Not Found\r\n"
                  "Content-Type: text/html\r\n"
                  "Connection: close\r\n"
                  "\r\n"
                  "<h1>404 Not Found</h1>"
               ).encode("utf-8")
               client.sendall(response)
        except Exception as error:
               print(f"Error: {error}")
        finally:
               client.close()

    # create socket server  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         sock.bind(("127.0.0.1", 0))
         sock.listen()
         print(f"Listening in port: {sock.getsockname()[1]}\n")
         while True:
               client_socket, address = sock.accept()
               print("Conection established:", address)
               threading.Thread(target=client_connection, args=(client_socket, path)).start()

socket_server(path)
