import sys
import socket
import struct


def upld_op(sock, file_name):
    try:
        file_obj = open(file_name, 'r')
    except:
        print 'Can not open file!'
    else:
        data = file_obj.read()
        file_obj.close()
        sock.send(struct.pack('!I', len(data)))
        sock.send(data)
        len_data, = struct.unpack('!I', sock.recv(4))
        print sock.recv(len_data)
    return


def dwnd_op(sock):
    file_name = str(raw_input("Enter the name by which you want to store the file: "))
    file_obj = open(file_name, 'a+')
    len_data, = struct.unpack('!I', sock.recv(4))
    file_obj.write(sock.recv(len_data))
    file_obj.close()
    return


def send_op(sock, data):
    sock.send(struct.pack('!I', len(data)))
    sock.send(data)
    return


def cli_op(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock


def main():
    sock = cli_op(str(sys.argv[3]), int(sys.argv[4]))
    send_op(sock, str(sys.argv[1]))
    send_op(sock, str(sys.argv[2]))
    if str(sys.argv[1]) == '-d':
        dwnd_op(sock)
    elif str(sys.argv[1]) == '-u':
        upld_op(sock, str(sys.argv[2]))
    return


main()
