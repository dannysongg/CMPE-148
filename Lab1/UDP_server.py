import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Created")

port = 4500

s.bind(('localhost', port))
print("Socket bound to port " + str(port))

print("UDP is listening")

while True:
    incoming = s.recvfrom(1024)
    data = incoming[0]
    address = incoming[1]
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
    s.sendto(''.join(result).encode(), address)
    if not data:
        break