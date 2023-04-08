import socket
import time

with open(r"Input\car.text","r") as file:
    car_list = file.readlines()

if __name__ == "__main__":
    PORT = 1234


    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind(("127.0.0.1",PORT))
    #put the socket into listening mode
    server.listen(5)

    while True:
        client , address = server.accept()
        print(f"Connection Established - {address[0]}:{address[1]}")

        for car in car_list:
            time.sleep(0.5)
            client.send(bytes(str(car),"utf-8"))

        client.close()
        break

    server.stop()

        

    


    