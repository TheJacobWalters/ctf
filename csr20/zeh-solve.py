#!/usr/bin/env python
import angr
import claripy
import random
import socket
# connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('chal.cybersecurityrumble.de', 65123))
    data = s.recv(1024)
    data = data[:-1]
    rando = int(data)
    k = 13
    e = 0
    for x in range(7):
        k = rando >> (k % 3)
    e = k ^ 53225
    inputs = '13 ' + str(e) + '\n'
    s.send(bytes(inputs, 'utf-8')) 
    flag = str(s.recv(1024))
    print(flag)
