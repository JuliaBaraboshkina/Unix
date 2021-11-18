#!/usr/bin/bash/env python
# -*- coding: utf-8 -*-

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9090))
client_list = []
print('Запуск сервера')
while True:
    data, addr = sock.recvfrom(1024)
    if addr not in client_list:
        client_list.append(addr)
    for client in client_list:
        if client != addr:
            sock.sendto(data, client)
print('Завершение работы сервера')