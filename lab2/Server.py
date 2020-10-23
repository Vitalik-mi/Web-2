import socket
import sys
import argparse
import time
import threading
import datetime
import json

send_code = False
cycle = False
user_list = []
data_timer = ""


def wait():
    global data_timer
    global send_code
    data_timer = str(datetime.datetime.now())
    time.sleep(11)
    send_code = True


def start_server(port):
    global cycle
    global send_code
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR, 1)
    print(f"Starting up server  on  port ('localhost', {port})")
    sock.bind(('localhost', port))
    sock.listen()
    while 1:
        print("Waiting to receive message from user")
        cycle = True
        user, address = sock.accept()
        data = user.recv(2048)
        dict_data = (json.loads(data.decode()))
        user_list.append(dict_data['Name'])

        user_accept_socket = threading.Thread(target=wait)
        user_accept_socket.start()

        dict_data["time-connect"] = str(datetime.datetime.now())
        dict_data["time-timer"] = data_timer

        send_json = json.dumps(dict_data)
        print(f"Data:{send_json}")
        cycle = False
        while cycle == False:
            if send_code == True:
                user.send(send_json.encode())
                print(f"sent {data} bytes back to {address}")
                break
        send_code = False
    user.close()


if __name__ == '__main__':
    port = 8585
    start_server(port)
