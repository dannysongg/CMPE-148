import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 4000

s.connect(('localhost', port))

print(s.recv(1024))

file = open('testCases.txt', 'r')
lines = file.readlines()
for line in lines:
    # print(line)
    line.strip()
    s.sendall(line.encode())

while True:
    result = s.recv(1024)
    print(result.decode())
    if not result:
        break

s.close()
