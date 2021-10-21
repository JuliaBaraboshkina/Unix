#!/usr/bin/bash/env python
# -*- coding: utf-8 -*-

import socket
import threading

def listening(sock):
     while True:
         data, server = sock.recvfrom(1024)
         print(data.decode())

name = input("Введите имя: ")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto((f"{name} -> Присоединился ").encode(), ('localhost', 9090))
threading.Thread(target = listening, args = (sock, )).start()
print('Начало беседы')
while True:
    msg = input("Введите сообщение: ")
    sock.sendto((name+": "+msg).encode(), ('localhost', 9090))