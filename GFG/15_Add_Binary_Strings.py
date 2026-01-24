
def addBinary(s1, s2):
    # code here
    
    b1 = int(s1,2)
    b2 = int(s2,2)
    
    s = b1 + b2
    
    return bin(s)[2:]


inpt = {'s1' :"1101", 's2' : "111", 's3' : "00100", 's4' : "010"}
for i in inpt.keys():
    print("String 1: ",inpt.get(i)," String 2: ",inpt[i])
    print("Output: ",addBinary(inpt.get(i),inpt[i]))
