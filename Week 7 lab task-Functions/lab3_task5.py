def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

print("GCD of 48 and 18:", gcd(48, 18))
print("LCM of 48 and 18:", lcm(48, 18))

'''output-
GCD of 48 and 18: 6
LCM of 48 and 18: 144
'''
