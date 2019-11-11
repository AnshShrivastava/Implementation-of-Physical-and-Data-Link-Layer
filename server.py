import socket			 
from crc import decodeData
from line_encoding import voltage_to_decode 
#Creating Server Socket
s = socket.socket()		 
print ("Socket successfully created")
port = 6011				 
s.bind(('', port))		 
print ("socket binded to %s" %(port)) 
s.listen(5)	 
print ("socket is listening")			
while True:
    #Connecting Client to Server  
    c, addr = s.accept()	 
    print ('Got connection from', addr)
    #Recieving Voltage from Sender  
    raw_data = c.recv(1024)
    if (raw_data.decode('utf-8') == 'EXIT'):
        break
    else:
        #Printing recieved voltage from sender
        print(raw_data)
        voltage = str(raw_data.decode())
        #Decoding voltage to bits
        data = voltage_to_decode(voltage)
        if not data:
            break
        key = "1001"
        #Decoding bits to check error through CRC-Encoding
        ans = decodeData(data, key)
        print("Remainder after decoding is "+ans)
        temp = "0"*(len(key)-1)
        #Sending Acknowledgement to Sender
        if ans == temp:
            c.sendall(b'Received data, NO ERROR FOUND')
        else:
            c.sendall(b'ERROR DETECTED') 
#closing connection
print("Closing Connection...")
c.close() 
