import random
import sys

def generateRandomVectors(nVec, dem, low=-1000000, high=1000000):
    """
    Generate random high-dimensional vectors with specified parameters

    Args:
        nVec (int): Number of vectors to be generated, must be a positive integer
        dem (int): Feature dimension of each vector, must be ≥1
        low (int, optional): Minimum value for random numbers, defaults to -1e6
        high (int, optional): Maximum value for random numbers, defaults to 1e6

    Raises:
        ValueError: nVec/dem are invalid / low > high

    Returns:
        list[list]: 2D list containing nVec vectors, each sublist contains dem float values within [low, high] range.
    """
    
    # Judge 
    if dem < 1 or nVec < 1:
        raise ValueError("Invlaid Value as Demensions")
    if not low <= high:
        raise ValueError("Invlaid Values for boarders")
    
    vectors=[[] for _ in range(nVec)]
    for i in range(nVec):
        for j in range(dem):
            vectors[i].append(random.randint(low,high))
    return vectors

def outputVectors(vectors):
    for i,vector in enumerate(vectors):
        print(i+1,end="th vector\n")
        for j in vector:
            print(j,end=" ")
        print("\n")

if __name__ == "__main__":
    # argvs = sys.argv
    # if len(argvs) !=3 and len(argvs) !=5:
    #     print("Error!\ngenerateMap.py <nVec> <dem> <minVal (-1e6 as default)> <maxVal (1e6 as default)>")
    #     sys.exit(1)
        
    # nVec = int(argvs[1])
    # dem = int(argvs[2])
    # low=-1000000
    # high=1000000
    # if len(argvs) == 5:
    #     low=int(argvs[3])
    #     high=int(argvs[4])
            
    Vectors=generateRandomVectors(5,2,11,44)
    outputVectors(Vectors)