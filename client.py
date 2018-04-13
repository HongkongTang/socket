import socket
import time
s = socket.socket()
#设置地址
host = socket.gethostname()
port = 1235

#链接服务端
s.connect((host,port))

#开始会话
while True:
	print s.recv(1024)
	s.send(raw_input('input:\n'))
s.close()