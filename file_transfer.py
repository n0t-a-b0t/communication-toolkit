import sys
import socket
import struct


def recv_fn(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    len_data, = struct.unpack('!I', conn.recv(4))
    return conn, conn.recv(len_data)


def send_file(conn, file_name):
    try:
        file_obj = open(file_name, 'r')
    except:
        message = 'Oops! Something went wrong... :P'
        conn.send(struct.pack('!I', len(message)))
        conn.send(message)
    else:
        data = file_obj.read()
        file_obj.close()
        conn.send(struct.pack('!I', len(data)))
        conn.send(data)
    return


def send_fn(file_path, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(struct.pack('!I', len(file_path)))
    s.send(file_path)
    return s


def recv_file(sock):
    len_data, = struct.unpack('!I', sock.recv(4))
    file_obj = open(str(sys.argv[3]), 'w+')
    file_obj.write(sock.recv(len_data))
    file_obj.close()
    return


def main():
    if str(sys.argv[1]) == '-fc':
        sock = send_fn(str(sys.argv[2]), str(sys.argv[4]), int(sys.argv[5]))
        recv_file(sock)
    elif str(sys.argv[1]) == '-fs':
        conn, file_name = recv_fn(str(sys.argv[2]), int(sys.argv[3]))
        send_file(conn, file_name)
    return


main()
