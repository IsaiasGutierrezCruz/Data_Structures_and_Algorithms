import sys

def gcd_Fast(a, b):
    if b == 0: 
        return a
    return gcd_Fast(b, a%b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_Fast(a, b))
