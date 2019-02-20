from math import gcd as bltin_gcd

def primRoots(modulo):
    required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo) }
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

print(primRoots(17))
'''
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

if __name__ == "__main__":
    p = 17
    primitive_roots = primRoots(p)
    print(primitive_roots)
'''
'''
打印原根
'''