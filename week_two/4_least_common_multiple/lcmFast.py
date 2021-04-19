import sys

def gcd_Fast(a, b):
    if b == 0: 
        return a
    return gcd_Fast(b, a%b)

def lcm_Fast(a, b):
    gcd = gcd_Fast(a, b)
    return int(a*b/gcd)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_Fast(a, b))

