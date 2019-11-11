import socket			 
from crc import encodeData
from line_encoding import encoding_to_voltage, errorgenerator
from frame import make_frame
#Specifying the value of end delimiter
ED = 11111
#Genrating Socket
s = socket.socket()		 
port = 6011				
s.connect(('127.0.0.1', port))
print("Connected to Server...") 
print("Press [1] to send a message\nPress [2] to send message with error\n")
char = input()
if char == '1':
    #Taking input to transmit from the user
    input_data = input("Enter data you want to send:")
    data =(''.join(format(ord(x), 'b') for x in input_data)) 
    print ("Message in bits: "+data) 
    #Defining key for CRC-Encoding
    key = "1001"
    #Encoding Data
    ans = encodeData(data,key) 
    #Printing Encoded Data
    print("Encoded data: "+ans)
    #Making frame from the encoded data
    ans = make_frame(ans)
    #Line-Encoding Frame
    ans = encoding_to_voltage(ans)
    print("Voltage: "+ans)
    #Converting encoded data to byte format to send through sockets
    output = ans.encode()
    #print("to send: ", output)
    #Sending Data through a socket 
    s.sendall(output)
    #Recieving acknowledgement about whether data received is error free or not and printing it
    acknowledgement = s.recv(1024)
    acknowledgement = acknowledgement.decode('utf-8')
    print (acknowledgement)
elif char == '2':
    #Taking input to transmit from the user
    input_data = input("Enter data you want to send:")
    data =(''.join(format(ord(x), 'b') for x in input_data)) 
    print ("Message in bits: "+data) 
    #Defining key for CRC-Encoding
    key = "1001"
    #Encoding Data
    ans = encodeData(data,key) 
    #Printing Encoded Data
    print("Encoded data: "+ans)
    #Making frame from the encoded data
    ans = make_frame(ans)
    #Line-Encoding Frame
    ans = encoding_to_voltage(ans)
    print("Voltage: "+ans)
    #Converting encoded data to byte format to send through sockets
    #Inducing error in transmitting
    ans = errorgenerator(ans)
    output = ans.encode()
    #print("to send: ", output)
    #Sending Data through a socket 
    s.sendall(output)
    #Recieving acknowledgement about whether data received is error free or not and printing it
    acknowledgement = s.recv(1024)
    acknowledgement = acknowledgement.decode('utf-8')
    print (acknowledgement)
   
#Closing the socket and connection
print("Closing Connection...")
s.close()	 
