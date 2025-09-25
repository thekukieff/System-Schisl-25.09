import string


def Sum(number):
    sum = 0
    for x in str(number):
        sum+=int(x)
    return sum

def convert_to(number, base):
    alphabet = "0123456789"+string.ascii_lowercase

    s = ''
    while number>0:
        s = alphabet[number%base]+s
        number//=base
    return s



# 5686 #5+
# 902 #6+
# 1303 #7 +
# 5324 #8+
# 16 #9+
# 6 #10+
# 849 #11+
# 127 #12+
# 24 #13+
# 4 #14+
#2 #15+
# 3 #16+
# 32 #17+
# 6 #18+





# print(str(convert_to(81**18 - (81**8 - 1)*((8+1)**8+1)//8-8, 3)).count("1"))#15
#
# print(Sum(str(convert_to(5*216**1256 - 5*36**1146 + 4*6**1053 - 1087, 6))))#12642
#
# print(Sum(convert_to(103*7**103 - 5*7**57 + 98, 7)))#280
#
# print(Sum(convert_to(6*343**1156 - 5*49**1147+4*7**1153 - 875, 7)))#13950
#
#
# print(Sum(convert_to(7**1003+6*7**1104 - 3* 7**57 + 294, 7)))#5686

# print(Sum(convert_to(4**1503 + 3*4**244 - 2 * 4**1444 - 96, 4)))#902

print(Sum(convert_to(6**1333 - 5*6**1215 + 3*6**144 - 86, 6)))


# print(Sum(convert_to(7**2103 - 6*7**1270+3*7**57 - 98, 7)))#5324
#
# #N9; 16
# for x in range(1,1000):
#     s = 64**11-4**10+96-x
#     sum_ = Sum(convert_to(s,4))
#     if sum_ == 71:
#         print(x)
#         break
#
# #N10; 6
# for x in range(1,1000):
#     s = 27**7-3**11+36-x
#     sum_ = Sum(convert_to(s,3))
#     if sum_ == 22:
#         print(x)
#         break
#
#
# #N11; 849
# for x in range(1,1000):
#     s = 125**7-25**4+x
#     temp = convert_to(s,5)
#     #sum_ = Sum(convert_to(s,3))
#     if temp.count("4") == 15 and temp.count("3") == 1 and temp.count("1") == 2:
#         print(x)
#         break
#
# #N12; 127
# for x in range(1,1000):
#     s = 64**12-8**14+x
#     temp = convert_to(s,8)
#     #sum_ = Sum(convert_to(s,3))
#     if temp.count("7") == 12 and temp.count("1") == 1:
#         print(x)
#         break
#
# #N13 24
# for x in range(1,1000):
#     s = 81**20-9**x+50
#     sum_ = Sum(convert_to(s,9))
#     if sum_ == 138:
#         print(x)
#         break
#
#
#
#
#
# #N14; 4
# print(convert_to(32**2 + 1024 + 1024**2, 16).count("0"))
#
# #N15; 11
# print(convert_to(26**2 + 169 - 11, 13).count("c"))
# print(convert_to(26**2 + 169 - 11, 13).count("2"))
#
# #N16; 21
# print(convert_to(7**2 + 49**4 - 21, 14).count("a"))
# print(convert_to(7**2 + 49**4 - 21, 14).count("0"))
#
# #N17 32
# summ = 0
# for x in range(2,11):
#     cont = True
#     num = convert_to(78,x)
#     for i in range(1, len(num)):
#         if (int(num[i-1])%2==0) and (int(num[i])%2 == 0) or (int(num[i-1])%2!=0) and (int(num[i])%2 != 0):
#             cont = False
#     if cont:
#         summ+=x
#
# print(summ)
#


# N18 6
arr = []

for x in range(2,11):
    temp = convert_to(1234,x)
    print(x, Sum(temp), temp)
    arr.append(Sum(temp))
print(arr)
print(max(arr))





