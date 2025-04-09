import random
import sys

def normalGenerate(nNodes, nEdges, isDirected, maxVal=0, negVal=False): 
    """
    Generate a normal Graph

    Args:
        nNodes (int): sum of Nodes
        nEdges (int): sum of Edges
        maxVal (int): maxVal 
        negVal (int): maxVal
    Returns:
        Edges (set(tuple(2) / tuple(3) )) : Generated DIRECTED edges with or without values
    """
    Edges=set()
    while len(Edges) < nEdges:
        u, v = random.sample(range(1,nNodes+1), 2)
        edge = (u, v)
        if not isDirected and u > v:
            edge = (v, u)
            
        if edge in Edges:
            continue
        if maxVal == 0:
            Edges.add(edge)
        else:
            Edges.add((edge[0],edge[1],randomNumber(maxVal,negVal)))
    return Edges

def listGenerate(nNodes,maxVal=0, negVal=False):
    """
    Generate a normal Graph

    Args:
        nNodes (int): sum of Nodes
        maxVal (int): maxVal 
        negVal (int): maxVal
    Returns:
        Edges (set(tuple(2) / tuple(3) )) : Generated DIRECTED edges with or without values
    """
    Edges=set()
    if maxVal == 0:
        for i in range(1,nNodes):
                Edges.add((i,i+1))
    else:
        for i in range(1,nNodes):
                Edges.add((i,i+1,randomNumber(maxVal,negVal)))
    return Edges
    
def flowerGenerate(nNodes,maxVal=0, negVal=False):
    """
    Generate a normal Graph

    Args:
        nNodes (int): sum of Nodes
        maxVal (int): maxVal 
        negVal (int): maxVal
    Returns:
        Edges (set(tuple(2)) | set(tuple(3)) )) : Generated DIRECTED edges with or without values
    """
    Edges=set()
    if maxVal == 0:
        for i in range(2,nNodes+1):
                Edges.add((1,i))
    else:
        for i in range(2,nNodes+1):
                Edges.add((1,i,randomNumber(maxVal,negVal)))
    return Edges

def randomNumber(maxVal, negVal):
    """
    generate random integer

    Args:
        maxVal (int) : maxVal
        negVal (bool) : negVal

    Returns:
        ret(int) : returned integer
    """
    if negVal == True:
        return random.randint(-maxVal,maxVal)
    if negVal == False:
        return random.randint(1,maxVal)


def generateRandomGraph(nNodes, nEdges, isDirected=False, maxVal=0, negVal=False, feat="normal", style="edge"):
    """
    Generate a random Graph

    Args:
        nNodes (int): sum of Nodes
        nEdges (int): sum of Edges
        isDirected (bool, optional): generated map is directed. Defaults to False.
        maxVal (int,optional): the max value of the edge. Defaults to 0, means no value.
        negVal (bool, optional): allow  negative value. Defaults to False.
        feat (normal / list / flower): the feature of the map. Deafaults to normal
        style (edge / map): the style of output. Defaults to edge.

    Raises:
        ValueError: nNodes and nSums are invalid

    Returns:
        Edges (list[tuple(2)] | list [tuple(3)]) : Return generated edges if style=edge
        
        Maps (list[list] | list[list[tuple(2)]]) : Return generated maps if style=map
    """ 
    
    if nEdges > nNodes * (nNodes - 1) // 2 and not isDirected:
        raise ValueError("Invlaid Values for Directed graph")
    if nEdges > nNodes * (nNodes - 1) and isDirected:
        raise ValueError("Invlaid Values for Indirected graph")
    if nNodes <=0 or nEdges < 0:
        raise ValueError("Invlaid Values of nodes or edges")

    # Init  
    Edges=set()
    
    # Generating edges & values
    if feat == "list": 
        Edges=listGenerate(nNodes,maxVal,negVal)
    elif feat == "flower": 
        Edges=flowerGenerate(nNodes,maxVal,negVal)
    elif feat == "normal":
        Edges=normalGenerate(nNodes,nEdges,isDirected,maxVal,negVal)
    else:
        raise ValueError("Wrong feature detected!")
        
    # Output 
    if style == "edge":
        return list(Edges)
        
    elif style == "map":
        Maps=[[] for _ in range(nNodes+1)]
        if maxVal == 0:
            for u,v in Edges:
                Maps[u].append(v)
                if not isDirected:
                    Maps[v].append(u)
        else:
           for u,v,w in Edges:
                Maps[u].append((v,w))
                if not isDirected:
                    Maps[v].append((u,w))
        return Maps
    else:
        raise ValueError("Wrong style detected!")
    

def outputGraphInWords(graph,style,maxVal):
    if style == "map":
        print("Map Are as follows:")
        if maxVal == 0:
            for u,mp in enumerate(graph):
                if u == 0:
                    continue
                print(f"Node {u}:")
                for v in mp:
                    print(f"to {v}");
        else:
            for u,mp in enumerate(graph):
                if u == 0:
                    continue
                print(f"Node {u}:")
                for (v,w) in mp:
                    print(f"to Node {v} , val={w}");
                
    elif style == "edge": 
        print("Edges are as follows:")
        if maxVal == 0:
            for i,edge in enumerate(graph):
                print (f"Edge {i+1}: {edge[0]} to {edge[1]}")
        else:
            for i,edge in enumerate(graph):
                print (f"Edge {i+1}: {edge[0]} to {edge[1]} val={edge[2]}")
            
                
def outputGraph(graph,style):
    """
    Output the graph according to given style.
    
    edge:
        n
        p_1 q_1
        p_2 q_2
        ...
    
    map:
        p_1 n_1 q_1,1 q_1,2 ...
        ...

    Args:
        graph (list[tuple] | list[list]): graph generated by generateRandomGraph
        style (map / edge): style of the graph
    """
    if style == "map":
        for i, neighbors in enumerate(graph):
            print(i,len(neighbors),sep=" ",end=" ") 
            for j in neighbors:
                print(j,end=" ")
            print()
                
    elif style == "edge": 
        print(len(graph))
        for edge in graph:
            print (edge[0],edge[1],sep=" ")


# Directly generate

if __name__ == "__main__":
    graph = generateRandomGraph(nNodes=4000,nEdges=500000,maxVal=105,isDirected=True,style="map")
    outputGraphInWords(graph,style="map",maxVal=105)
        
    # argvs = sys.argv
    # if len(argvs) <= 2 or len(argvs) >= 7:
    #     print("Error!\ngenerateMap.py <nNodes> <nEdges> <isDirected ( true / false(Default) )>  \n <feat (normal / list / flower) > <style ( edge(Default) / map) >")
    #     sys.exit(1)
        
    # nNodes = int(argvs[1])
    # nEdges = int(argvs[2])
    # isDirected = False
    # feat = "normal" 
    # style = "edge"
    # _maxVal=100000
    # for i in range(3,len(argvs)):
    #     opt = argvs[i].strip().lower()
    #     if opt == "false" or opt == "true":
    #         isDirected = opt == "true"
    #     elif opt == "normal" or opt == "list" or opt == "flower":
    #         feat = opt 
    #     elif opt == "map" or opt == "edge":
    #         style = opt 
            

    # print("Generating Parameters:")
    # print(nNodes, nEdges, isDirected, feat, style,sep="   ",end="\n\n")
    # try:
    #     graph = generateRandomGraph(nNodes, nEdges, isDirected, feat, style,maxVal=_maxVal)
    #     outputGraphInWords(graph,style,_maxVal)
        
    # except ValueError as e:
    #     print(f"Error: {e}")