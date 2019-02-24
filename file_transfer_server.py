import sys
import socket
import struct
import os


def split_path(file_name):
    al01 = []
    while True:
        parts = os.path.split(file_name)
        if parts[0] == file_name:  # sentinel for absolute paths
            al01.insert(0, parts[0])
            break
        elif parts[1] == file_name:  # sentinel for relative paths
            al01.insert(0, parts[1])
            break
        else:
            file_name = parts[0]
            al01.insert(0, parts[1])
    return al01


def file_recv(conn, file_name):
    al02 = split_path(file_name)
    num01 = len(al02) - 1
    file_name = al02[num01]
    try:
        file_obj = open(file_name, 'a+')
    except:
        message = 'Can not perform upload to the server directory!'
        conn.send('!I', len(message))
        conn.send(message)
    else:
        len_data, = struct.unpack('!I', conn.recv(4))
        file_obj.write(conn.recv(len_data))
        file_obj.close()
        message = 'File uploaded successfully!'
        conn.send(struct.pack('!I', len(message)))
        conn.send(message)
    return


def file_send(conn, file_name):
    try:
        file_obj = open(file_name, 'r')
    except:
        message = "No such file!"
        conn.send(struct.pack('!I', len(message)))
        conn.send(message)
    else:
        data = file_obj.read()
        file_obj.close()
        conn.send(struct.pack('!I', len(data)))
        conn.send(data)
    return


def recv_op(conn):
    len_data, = struct.unpack('!I', conn.recv(4))
    return conn.recv(len_data)


def serv_op(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    return sock.accept()


def main():
    conn, addr = serv_op(str(sys.argv[1]), int(sys.argv[2]))
    op = recv_op(conn)
    file_name = recv_op(conn)
    if str(op) == '-d':
        file_send(conn, str(file_name))
    elif str(op) == '-u':
        file_recv(conn, str(file_name))
    return


main()
