import random
import sys
import os

# accept the number of tests as a command line parameter 
tests = int(sys.argv[1])
# accept the parameter for the tests as a command line parameter 
n = int(sys.argv[2])

for i in range(tests):
    print("Test #" + str(i))
    # run the generator gen.py with parameter n and the seed i
    os.system("python3 gen.py " + str(n) + " " + str(i) + " > input.txt")
    # run the model solution model.py
    # Notice that it is not necessary that solution is implemented in 
    # python, you can as well run ./model < input.txt for a c++ solution
    os.system("python3 fibonacciNaive.py < input.txt > fibonacciNaive.txt")
    # run the main solution 
    os.system("python3 fibonacciFast.py < input.txt > fibonacciFast.txt")

    # read the output of the model solution: 
    with open('fibonacciNaive.txt') as f: model = f.read()
    print("fibonacciNaive: ", model)
    # read the output of the main solution
    with open('fibonacciFast.txt') as f: main = f.read()
    print("fibonacciFast: ", main)
    if model != main:
        break

