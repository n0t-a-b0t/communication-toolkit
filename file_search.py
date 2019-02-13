import sys
import platform
import os
import re
import socket
import struct

global alpha


def send_data(sock, file_name):
    sock.send(struct.pack('!I', len(file_name)))
    sock.send(file_name)
    return


def recv_data(sock):
    global len_data
    len_data, = struct.unpack('!I', sock.recv(4))
    return sock.recv(len_data)


def results(op_string):
    if str(sys.argv[1]) == '-l':
        print op_string
    elif str(sys.argv[1]) == '-fs':
        send_data(alpha, op_string)
    return


def for_sys_serv(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    global alpha
    alpha = c
    file_name = recv_data(c)
    search_engine(file_name)
    return


def for_sys_cli(file_name, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    send_data(s, file_name)
    try:
        while recv_data(s) != '':
            print recv_data(s)
    except:
        print "Done!"
    return


def search_engine(file_name):
    if platform.system() == 'Linux':
        path = '/'
    elif platform.system() == 'Windows':
        path = 'C:\\'
    else:
        print "System not supported..."
        return

    pattern_obj = re.compile(file_name)
    counter01 = True
    counter02 = 0
    while counter01:
        for root, dirs, files in os.walk(path):
            for i in files:
                if re.search(pattern_obj, i):
                    results(os.path.join(root, i))
                    counter01 = False
                else:
                    if platform.system() == 'Linux':
                        try:
                            path = (path+'/'+dirs[counter02])
                        except:
                            counter02 += 1
                    elif platform.system() == 'Windows':
                        try:
                            path = (path+'\\'+dirs[counter02])
                        except:
                            counter02 += 1
    return


def main():
    if str(sys.argv[1]) == '-l':
        search_engine(str(sys.argv[2]))
    elif str(sys.argv[1]) == '-fc':
        for_sys_cli(str(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]))
    elif str(sys.argv[1]) == '-fs':
        for_sys_serv(str(sys.argv[2]), int(sys.argv[3]))
    else:
        print "Bad arguments..."
    return


main()
