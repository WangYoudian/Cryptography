from math import gcd

print(gcd(8765,23485))
'''
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
'''