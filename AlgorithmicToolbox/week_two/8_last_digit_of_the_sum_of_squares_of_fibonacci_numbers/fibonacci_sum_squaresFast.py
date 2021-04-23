from sys import stdin

def fibonacci_sum_squares_Fast(n):
    if n <= 1:
        return n

    rem = n % 60
    numbersFibonacci = [0, 1]
    if (n >= 2):
        for i in range(2, rem + 2):
            numbersFibonacci.append(numbersFibonacci[i-1] + 
            numbersFibonacci[i-2])
    # do not need to arrive to n, only to rem 
    return (numbersFibonacci[rem]*numbersFibonacci[rem + 1]) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_Fast(n))