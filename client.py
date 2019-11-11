import socket			 
from crc import encodeData
from line_encoding import encoding_to_voltage, errorgenerator
#Genrating Socket
s = socket.socket()		 
port = 6011				
s.connect(('127.0.0.1', port))
print("Connected to Server...") 
while True:
    print("Press [1] to send a message\nPress [2] to send message with error\nPress any other key to close connection")
    char = input()
    if char == '1':
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
        #Line-Encoding Bits
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
    if char == '2':
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
        #Line-Encoding Bits
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
    else:
        break
#Closing the socket and connection
print("Closing Connection...")
out = 'EXIT'
s.sendall(out.encode('utf-8'))
s.close()	 
