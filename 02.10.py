from string import ascii_lowercase, ascii_uppercase
def convert_to(number, base):
    alphabet = "0123456789"+ascii_lowercase+ascii_uppercase+"#$"
    temp = ''
    while number>0:
        temp = alphabet[number%base] + temp
        number //= base
    return temp

def Sum(num):
    temp = 0
    num = str(num)
    for x in num:
        temp+=int(x)
    return temp

# N2 = 86130
# arr = []
# for x in range(54, -1,-1):
#    num = 55**3*35 + 55**2*x + 55*34 + 33 - (2*55**3+33*55**2+x*55**1+34)
#    if num%29 == 0:
#        arr.append(num)
# print(abs(max(arr)-min(arr)))


#N3 = 4
# count_ = 0
# for x in range(79,-1,-1):
#     num1 = 5*x**4 + 5*x**3 + x**2 + x + 3
#     num2 = 7*80**3 + x*80**2 + x*80 + 5
#     if abs(num1-num2)<1000000:
#         count_ +=1
# print(count_)

# #N4 = 9
# count_ = 0
# for x in range(6,101):
#     num1 = x**4 + 3*x**3 + x**2 + 5*x + 2 + 7*100**3 + x*100**2 + 2*100 + 5
#     if num1 %11 == 0:
#         count_+=1
# print(count_)

# N5 = 1535
# arr = []
# for x in range(14):
#     for y in range(14):
#         M = 2*15**5 + y*15**4 + 2*15**3 + 3*15**2 + x*15 + 5
#         N = 6*13**4 + 7*13**3 + x*13**2 + 9*13 + y
#         A = N-M%N
#         arr.append(A)
# print(min(arr))


# #N6 = 552647
# arr = []
# for x in range(12):
#     for y in range(12):
#         M = 7*25**5 + y*25**4 + 2*25**3 + 3*25**2 + x*25 + 5
#         N = 6*11**4 + 7*11**3 + x*11**2 + 9*11 + y
#         if (M+N)%131 == 0:
#             print((M+N)/131)


#N7 = 25871
# arr = []
# for x in range(26):
#     for y in range(14):
#         M =  x*22**4 + 2*22**3 + 3*22**2 + x*22 + 5
#         N = 6*13**4 + 7*13**3 + y*13**2 + 9*13 + y
#         if (M-N)%57 == 0:
#             print((M-N)/57)


#N8 = 1464

# for x in range(13):
#     num = 8*13**4 + x*13**3 + 1*13**2 + 2*13 + 1 - (7*13**4 + x*13**3 + 5*13**2 + 7*13 +5)
#     if num%19 == 0:
#         print( num/19)


#N9 = 7806
# for x in range(16):
#     num = 8*15**4 + 2*15**3 + x*15**2 + 15 + 9 - (6*15**4 + x*15**3 + 7*15 + 3)
#     if num%11 == 0:
#         print(num/11)
#


#N10 = 8767
# for x in range(16):
#     num = 15**4 + 2*15**3 + 3*15**2 + x*15 + 5 + 15**4 + x*15**3 + 2*15**2 + 3*15 + 3
#     if num%14 == 0:
#         print(num/14)


#N11 = 1625
# print(convert_to(7*729**543 - 6*81**765 - 5*9**987 - 20, 9).count("8"))


#N12 = 666
#print(convert_to(7*512**3200 + 6*256**3100 - 5*64**3000 - 4*8**2900 - 1542, 64).count("0"))

#N13 = 74
# print(convert_to(((7**80 - 7**4 + int("234" , 7))*5 * 8)//6, 7).count("4"))

# N14 = 3
# arr = []
# for x in range(1000):
#     num = int(convert_to(3*16**2018 - 2*8**1028 - 3*4**1100 - 4**x - 2022, 4))
#     S = Sum(num)
#     if num>0:
#         arr.append(S)
# print(len(set(arr)))


# #N15 = 478
# num = convert_to(53**123 + 65**2222 - 172**12, 7)
# print(num.count("61")+ num.count("62")+ num.count("63")+ num.count("64")+ num.count("65"))

# #N16 = 175
# num = convert_to(8**888 + 15*15**1515 - 2**444, 8)
# print(num.count("71")+ num.count("72")+ num.count("73")+ num.count("74")+ num.count("75")+ num.count("76"))

#N18 = 257
#
# num = convert_to(49**129 + 7**131 - 2, 7)
# max_ = max(num)
# s = num.replace("0", max_)
# print(s.count(max_))


#N17 = 3

# print(convert_to(18**105 + 35 *16**100 - 3**51 + 15**90,16).count("66"))


#N19 = 10
# a = "qwe"
#
# num = 11*15**65 + 18*15**38 - 14 * 15**17 + 19*15**11 + 18338
# s = convert_to(num, 15)
#
# print(len(set(str(s))))