# Uses python3
import sys

def fibonacci_sum_Fast(n):
    if n <= 1:
        return n
    # Pisano period for % 10 is 60
    rem = n % 60

    if(rem == 0): 
        return 0
    
    f0 = 0
    f1 = 1
    for i in range (2, rem + 3): 
        f = (f0 + f1) % 60
        f0 = f1
        f1 = f
    suma = f1 - 1
    return suma % 10 

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_Fast(n))
