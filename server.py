import socket			 
from crc import decodeData
from line_encoding import voltage_to_decode
from frame import de_frame
#Specifying value of end-delimiter 
ED = 11111
#Creating Server Socket
s = socket.socket()	
print ("Server successfully created")
port = 6011				 
s.bind(('', port))		  
s.listen(5)	 
print ("Server is waiting for client...")			
while True:
    #Connecting Client to Server  
    c, addr = s.accept()	 
    print ('Got connection from', addr)
    #Recieving Voltage from Sender  
    raw_data = c.recv(1024)
    voltage = str(raw_data.decode())
    #printing received voltage from sender    
    print("Voltage:"+voltage)
    #Decoding voltage to frame
    data = voltage_to_decode(voltage)
    if not data:
        break
    key = "1001"
    print("Recieved Frame: "+data)
    #Decoding frame to Encoded-Data
    data = de_frame(data)
    #Decoding bits to check error through CRC-Encoding
    ans = decodeData(data, key)
    print("Remainder after decoding is "+ans)
    temp = "0"*(len(key)-1)
    #Sending Acknowledgement to Sender
    if ans == temp:
        c.sendall(b'Received data, NO ERROR FOUND')
    else:
        c.sendall(b'ERROR DETECTED')
    char = input("Press [Y] to close server, press any other key to continue")
    if char is 'Y':
        break
    else:
        print("__________________________________________________________________") 
#closing connection
print("Closing Connection...")
c.close() 
