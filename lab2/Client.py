import socket
import time
import threading
import datetime
import json
import sys
import argparse


def start_client(port):
    user_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    print(f"Connecting to port ('localhost', {port})" )
    user_socket.connect(('localhost', port))
    try:
        name = input("Введіть ім'я : ")
        num = input("Введіть ID : ")
        x = {"Name": name, "ID": num}
        send_json = json.dumps(x)
        print(f"Надіслано { send_json}")
        user_socket.sendall(send_json.encode())
        get_amount = 0
        pending_amount = len(send_json)

        print(pending_amount)
        while get_amount < pending_amount:
            data = user_socket.recv(1000)
            get_amount += len(data)
        print(f"Get: { data.decode()}")
    finally:
        print("Підключення до серверу завершено")
        user_socket.close()


if __name__ == '__main__':
    port = 8585
    start_client(port)
