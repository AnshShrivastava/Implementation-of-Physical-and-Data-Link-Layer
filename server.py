import socket			 
from crc import decodeData 
s = socket.socket()		 
print ("Socket successfully created")
port = 6011				 
s.bind(('', port))		 
print ("socket binded to %s" %(port)) 
s.listen(5)	 
print ("socket is listening")			
while True:  
    c, addr = s.accept()	 
    print ('Got connection from', addr)  
    raw_data = c.recv(1024)
    print(raw_data)
    data = str(raw_data.decode())
    if not data:
        break
    key = "1001"
    ans = decodeData(data, key)
    print("Remainder after decoding is "+ans)
    temp = "0"*(len(key)-1)
    if ans == temp:
        c.sendall(b'Received data, NO ERROR FOUND')
    else:
        c.sendall(b'Error in data') 
    c.close() 
