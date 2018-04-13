import socket
import time
s = socket.socket()

host = socket.gethostname()
port = 1235

s.bind((host,port))
s.listen(5)

#接受客户端的链接，并得到客户端的套接字和地址
c,addr = s.accept()

#开始会话
while True:
	c.send(raw_input('input:\n'))
	print c.recv(1024)
c.close()


