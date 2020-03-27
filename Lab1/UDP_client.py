import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 4500

file = open('testCases.txt', 'r')
lines = file.readlines()
for line in lines:
    # print(line)
    line.strip()
    s.sendto(line.encode(), ('localhost', port))

while True:
    incoming = s.recvfrom(1024)
    result = incoming[0]
    print(result.decode())
    if not result:
        break

s.close()