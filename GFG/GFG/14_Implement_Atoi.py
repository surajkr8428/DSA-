
# def Implement_Atoi(s):
    
#     n = []
#     # s = s.strip(" ")
#     s = s.replace(" ", "")
#     sgn = []
    
#     if s[0] == "-":
#         sgn.append("-")
#     elif s[0] == "+":
#         sgn.append("+")
        
#     num = 0
#     for i in s:
#         if i.isdigit():
#             # n.append(int(i))
#             num *= 10
#             num += int(i)
    
    
#     # for i in n:
#     #     # num *= 10
#     #     # num += i
    
#     if sgn == "-":
#         num *= -1
        
#     if num > pow(2,31) - 1:
#         return pow(2,31) - 1

#     elif num < pow(2,31) * -1:
#         return pow(2,31) * -1

#     return num

def myAtoi(s: str) -> int:
    i = 0
    n = len(s)
    sign = 1
    num = 0

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # 1️⃣ Skip leading whitespaces
    while i < n and s[i] == ' ':
        i += 1

    # 2️⃣ Check sign
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # 3️⃣ Read digits
    while i < n and '0' <= s[i] <= '9':
        digit = ord(s[i]) - ord('0')
        num = num * 10 + digit

        # 4️⃣ Clamp overflow
        if sign * num >= INT_MAX:
            return INT_MAX
        if sign * num <= INT_MIN:
            return INT_MIN

        i += 1

    return sign * num

    
# 

lst = ["-123","  -"," 1231231231311133","-999999999999","  -0012gfg4",'-I5fI5']
for i in lst:
    print("Input: ",i)
    # print("Output: ",Implement_Atoi(i))
    print("Output: ",myAtoi(i))