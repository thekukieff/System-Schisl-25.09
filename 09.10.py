from string import ascii_lowercase, digits, ascii_uppercase,punctuation


def Sum(number):
    sum = 0
    for x in str(number):
        sum+=int(x)
    return sum

def convert_to(number, base):
    alphabet = "0123456789"+ascii_lowercase+ ascii_uppercase+punctuation+"абвгдежзийклмнопрстуфхцчшщъыьэю"
    s = ''
    while number>0:
        s = alphabet[number%base]+s
        number//=base
    return s
#N1 = 819869
# #
# res = 1
# for x in range(18,36):
#         res = int("22A12E", x) + int("2F1391", x) - int("1H05D0", x)
#
#         if res%19 == 0:
#             print(res/19)

# #N2 = 159792
# for x in range(7,36):
#     res = int("2465123", x) + int("251341", x)
#     if res%17 == 0:
#         print(res/17)


# 3319197720
# for x in "0123456789"+ascii_lowercase:
#     res = int("923"+x+"874", 29)+ int("524"+x+"6152", 29)
#     if res%28 == 0:
#         print(res/28)
#         break

#N4 = 3367
# count_ = 0
# res = convert_to(2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561, 27)
# for x in res:
#    if not(x in digits):
#        count_+=1
#        print(x)
# print(count_)

#N5 = 2394

#
# for x in range(1, 2401):
#     if convert_to(7*9**210 + 6*9**110 - x,9).count("0") == 100:
#         print(x)

# #N6 = 48
# alphabet = "0123456789"+ascii_lowercase
#
# res = convert_to(30*36**231 + 18*6**101 - 3*36**45 - 2357,36)
# count_= 0



# for x in res:
#     if (alphabet.index(x)%5 == 0 or alphabet.index(x)%3 == 0 and (alphabet.index(x)%5 != 0 or alphabet.index(x)%3 != 0)) :
#         if x != "0":
#             count_+=1
#             print(x)
# print(count_)

#N7 = 377
# res = convert_to(17*125**453+117*5**231 - 3*5**13 - 2357, 125)
#
# alphabet = "0123456789"+ascii_lowercase+"*"
# count_=0
# for x in res:
#     if x in alphabet:
#         count_+=1
# print(count_)


#N8 = 267
# count_= 0
# res = convert_to(2*2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35,49)
# for x in res:
#     if x in digits:
#         count_+=1
# print(count_)

# #N9 = 3
# res = convert_to(39*121**319+46*11**913 - 15*1331**15 - 1993,121)
#
# alphabet = "0123456789" + ascii_lowercase + ascii_uppercase + punctuation + "абвгдежзийклмнопрстуфхцчшщъыьэю"
# count_=0
#
# for x in res:
#     if alphabet.index(x) >=64 and alphabet.index(x) <=104:
#         count_+=1
#         print(x)
# print(count_)

#N10 = 81
#
# for x in range(1,3001):
#     res = convert_to(9**150+9**30 - x, 9)
#     if res.count("0") == 122:
#         print(x)


# #N11 = 2000
# for x in range(1,2006):
#     res = convert_to(4**163*5+12**62 - x,5)
#     if res.count("1")<res.count("4"):
#         print(x)
alphabet = "0123456789"+ascii_lowercase+punctuation
for x in range(42):
    x = str(x)
    res = int("j569"+x+"1"+x+"ia", 42)

    if res%155==0:
        print(res/155)


