import socket
import time
import sys



if __name__ == "__main__":
    
    print(sys.argv)
    if len(sys.argv) >= 2:
        with open(r"Input\%s.text" %(sys.argv[1]),"r") as file:
            data_list = file.readlines()
        
        PORT = int(sys.argv[2])
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        server.bind(("127.0.0.1",PORT))
        #put the socket into listening mode
        server.listen(5)

        while True:
            client , address = server.accept()
            print(f"Connection Established - {address[0]}:{address[1]}")

            for data in data_list:
                time.sleep(0.1)
                client.send(bytes(str(data),"utf-8"))

            client.send(bytes("stop","utf-8"))
            client.close()
            break
        
    else:
        print("arument is not provide: ",sys.argv[1:])

        

    


    