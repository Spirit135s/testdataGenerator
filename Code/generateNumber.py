import random
import sys

def generateRandomNumbers(n,low=-1000000, high=1000000):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(low,high))
    return numbers

def outputNumbers(numbers):
    for i in numbers:
        print(i)

if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) !=2 and len(argvs) !=4:
        print("Error!\ngenerateMap.py <Nums> <minVal (-1e6 as default)> <maxVal (1e6 as default)>")
        sys.exit(1)
        
    Nums = int(argvs[1])
    low=-1000000
    high=1000000
    if len(argvs) == 4:
        low=int(argvs[2])
        high=int(argvs[3])
            
    Numbers=generateRandomNumbers(Nums,low,high)

    outputNumbers(Numbers)