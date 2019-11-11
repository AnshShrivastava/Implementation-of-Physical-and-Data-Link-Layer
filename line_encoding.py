
def voltage_to_decode(s):
    l = len(s)
    ss=''
    for i in range(0,l):
            if s[i]=='+':
                #print(" 1 ")
                ss +='1'
            if s[i]=='-':
                ss +='0'
    return ss


def encoding_to_voltage(ss):
    l = len(ss)
    s = ''
    for i in range(0,l):
            if ss[i]=='0':
                #print(" -5 ")
                s = s + "-5"
            if ss[i]=='1':
                #print(" +5 ")
                s = s + "+5"
    return s
def errorgenerator(s):
    l = len(s)
    ss = ''
    for i in range(0, l):
        #print("debug")
        if i%4 == 0:
            if s[i]=='+':
                #print(" 1 ")
                ss +='-'
            if s[i]=='-':
                ss +='+'
        else:
            ss += s[i] 
    return ss