#!/usr/bin/python3
#coding:utf-8

import socket

host, port = ('localhost', 1234)



try:

    socket123 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket123.connect((host,port))
    print("client connecté !!!!")


    donnée = "BNjour à toi le client"
    donnée = data.encode(utf8)
    socket.sendall(donnée)



except : 
    print("connexion échoué")

finally:
    socket123.close()





































































































