import socket			 
from crc import encodeData
#Genrating Socket
s = socket.socket()		 
port = 6011				
s.connect(('127.0.0.1', port)) 
#Taking input to transmit from the user
input_data = input("Enter data you want to send:")
data =(''.join(format(ord(x), 'b') for x in input_data)) 
print (data) 
#Defining key for CRC-Encoding
key = "1001"
#Encoding Data
ans = encodeData(data,key) 
#Printing Encoded Data
print("Encoded data: "+ans)
#Converting encoded data to byte format to send through sockets
output = ans.encode()
print("to send: ", output)
#Sending Data through a socket 
s.sendall(output)
#Recieving acknowledgement about whether data received is error free or not and printing it
acknowledgement = s.recv(1024)
acknowledgement = acknowledgement.decode('utf-8')
print (acknowledgement)
#Closing the socket and connection
s.close()	 
