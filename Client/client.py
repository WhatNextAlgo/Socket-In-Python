import socket


if __name__ == "__main__":
    PORT = 1234
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect(("127.0.0.1",PORT))   

    while True:
        full_msg = server.recv(1024).decode("utf-8")
        print(full_msg)
        with open("Output/my_file.txt","a") as f:
            f.write(full_msg)
        
        full_msg = ""
