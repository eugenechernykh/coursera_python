a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
max1 = (a1//a2)*(b1//b2)*(c1//c2)
max2 = (a1//a2)*(b1//c2)*(c1//b2)
max3 = (a1//c2)*(b1//b2)*(c1//a2)
max4 = (a1//c2)*(b1//a2)*(c1//b2)
max5 = (a1//b2)*(b1//c2)*(c1//a2)
max6 = (a1//b2)*(b1//a2)*(c1//c2)
MAX = max(max1, max2, max3, max4, max5, max6)
print(MAX)