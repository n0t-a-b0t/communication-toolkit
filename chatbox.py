import sys
import socket
import select
import struct


def chatops(sock):
    while True:
        sock_list = [sys.stdin, sock]
        read_socket, write_socket, error_socket = select.select(sock_list, [], [])
        for i in read_socket:
            if i == sys.stdin:
                try:
                    msg = sys.stdin.readline()
                    sock.send(struct.pack('!I', len(str(msg))))
                    sock.send(str(msg))
                    sys.stdout.write("<You>")
                    sys.stdout.write(str(msg))
                    sys.stdout.flush()
                except:
                    continue
            else:
                len_msg, = struct.unpack('!I', sock.recv(4))
                print(sock.recv(len_msg))
    return


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if str(sys.argv[1]) == '-fs':
        s.bind((str(sys.argv[2]), int(sys.argv[3])))
        s.listen(1)
        conn, addr = s.accept()
        chatops(conn)
        conn.close()
    elif str(sys.argv[1]) == '-fc':
        s.connect((str(sys.argv[2]), int(sys.argv[3])))
        chatops(s)
        s.close()
    else:
        print "Bad arguments!"
    return


main()
