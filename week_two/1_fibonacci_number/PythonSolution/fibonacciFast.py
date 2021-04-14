def calc_fib(n):
    numbersFibonacci = [0, 1]
    if (n >= 2):
        for i in range(2, n +1):
            numbersFibonacci.append(numbersFibonacci[i-1] + 
            numbersFibonacci[i-2])
    return numbersFibonacci[n]

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
