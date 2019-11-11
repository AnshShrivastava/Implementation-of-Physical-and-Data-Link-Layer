#Function to make frame from a encoded data
def make_frame(string):
    data = []
    for i in range(0, len(string)):
        data.append(string[i])
    srr = '11111'
    N = len(data)
    i = 0
    while i < N:
        #print(i)
        if (i<N-3):
            if (data[i]==1, data[i+1]==1, data[i+2]==1, data[i+3]==1):
                srr += str(data[i])
                srr += str(data[i+1])
                srr += str(data[i+2])
                srr += str(data[i+3])
                srr += '0'
                i += 4
        else:
            srr += data[i]
            i += 1
    srr+='11111'
    return srr
#Convert frame into encoded data           
def de_frame(string):
    srr = ''
    data = []
    for i in range(0, len(string)):
        data.append(string[i])
    N = len(data)-5
    i = 5
    while i < N:
        #print(i)
        if (i<N-3):
            if (data[i]==1, data[i+1]==1, data[i+2]==1, data[i+3]==1):
                srr += str(data[i])
                srr += str(data[i+1])
                srr += str(data[i+2])
                srr += str(data[i+3])
                i += 5
        else:
            srr += data[i]
            i += 1
    return srr