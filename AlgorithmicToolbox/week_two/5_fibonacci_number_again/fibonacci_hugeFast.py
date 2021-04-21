import sys

def pissanoPeriod(m): 
    periodValues = [0, 1]
    for i in range(2, m * m + 1):
        periodValues.append((periodValues[i - 2] + 
        periodValues[i - 1]) % m)
        # begin of all pissano period 
        if (periodValues[i - 1] == 0 and periodValues[i] == 1):
            # remove the numbers of the next period and return it 
            return periodValues[0:i-1]

def get_fibonacci_huge_Fast(n, m):
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1
    periodValues = pissanoPeriod(m)
    # get the index where the result is keep   
    mod = n % len(periodValues)
    return periodValues[mod]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_Fast(n, m))