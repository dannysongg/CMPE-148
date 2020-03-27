import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

port = 4000

s.bind(('localhost', port))
print("Socket bound to port " + str(port))

s.listen(1)
print("Socket is listening")

c, addr = s.accept()
c.send(b'Connection established')

while True:
    data = c.recv(1024)
    years = data.decode().split()
    result = []
    for year in years:
        yearInt = int(year)
        if (yearInt % 4) == 0:  
            if (yearInt % 100) == 0:  
                if (yearInt % 400) == 0:  
                    result.append(year + ': Yes ')
                else:
                    result.append(year + ': No ')
            else:
                result.append(year + ': Yes ')
        else:
            result.append(year + ': No ')
    c.send(''.join(result).encode())
    if not data:
        break


c.close()