import sys
import socket
import struct
from thread import *

global client_list


def conn_thread(sock, info):
    while True:
        try:
            len_msg, = struct.unpack('!I', sock.recv(4))
            msg = sock.recv(len_msg)
            if msg:
                print(info[0]+" "+str(msg))
                broadcast(info[0]+" "+str(msg), sock)
            else:
                remove(sock)
        except:
            continue
    return


def remove(sock):
    if sock in client_list:
        client_list.remove(sock)
    return


def broadcast(message, sock):
    for i in client_list:
        if i != sock:
            try:
                i.send(struct.pack('!I', len(message)))
                i.send(message)
            except:
                i.close()
                remove(i)
    return


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((str(sys.argv[1]), int(sys.argv[2])))
    s.listen(100)
    global client_list
    client_list = []
    while True:
        conn, addr = s.accept()
        client_list.append(conn)
        print(addr[0]+' connected')
        broadcast((addr[0]+' connected'), conn)
        start_new_thread(conn_thread, (conn, addr))
    return


main()
