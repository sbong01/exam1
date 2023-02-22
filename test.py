#Part 2
#name: saerin bong

#Mid 11.
import math

def Trig(a,b,c):
    result = 2*math.pi*pow(a,3) + 3*math.sin(b) + 530.27 * math.sqrt(c + 34)
    return result

print(Trig(20,0,30))


#Mid 12.

def is_divisible_five(num):
    if num % 5 == 0:
        print("Yes, it is!")
    else:
        print("No, it is not!")



#Mid 13.
for x in range(3,10):
    result = math.sqrt(x) + 1
    print(result)
