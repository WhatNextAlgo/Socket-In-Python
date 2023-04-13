import socket
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 2:

        PORT = int(sys.argv[2])
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.connect(("127.0.0.1",PORT))   

        while True:
            full_msg = server.recv(1024).decode("utf-8")
            print(full_msg)
            if full_msg ==  "stop":
                break
            with open("Output/%s.txt" %(sys.argv[1]),"a") as f:
                f.write(full_msg)
            
            full_msg = ""

