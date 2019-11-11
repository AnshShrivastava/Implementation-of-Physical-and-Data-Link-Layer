def xor(a, b):  
    result = []  
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result)

def mod2div(divident, divisor):
    pick = len(divisor)
    temp = divident[0 : pick]
    while pick < len(divident):
        if temp[0] == '1':
            temp = xor(divisor, temp) + divident[pick]
        else:
            temp = xor('0'*pick, temp) + divident[pick]
        pick += 1
    if temp[0] == '1':
            temp = xor(divisor, temp)
    else:
            temp = xor('0'*pick, temp)
    checkword = temp
    return checkword

def encodeData(data, key):
    length_key = len(key)
    appended_data = data + '0'*(length_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

def decodeData(data, key):
    length_key = len(key)
    appended_data = str(data) + '0'*(length_key-1)
    remainder = mod2div(appended_data, key)
    return remainder