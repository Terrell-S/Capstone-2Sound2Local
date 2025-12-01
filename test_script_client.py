import networking as nt
import socket

sock = socket.socket()
sock.connect(('192.168.1.102',5000 )) #ip address of device running server. '127.0.0.1'   '192.168.1.102'

msg = ''
while True:
    print('waiting for update request...')
    in_msg = sock.recv(128).decode()
    print('received message:', in_msg)
    msg = input("enter update message: ")
    if msg == 'close':
        break
    sock.send(msg.encode())
    print('message sent')

print('goodbye')



