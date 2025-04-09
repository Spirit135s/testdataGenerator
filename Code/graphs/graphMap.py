import sys
import numpy as np
import random

    
def generateRandomGraph(nNodes, nEdges, isDirected=False):
    """
    Generate a random Graph

    Args:
        nNodes (int): sum of Nodes
        nEdges (int): sum of Edges
        isDirected (bool, optional): Tell if then map is directed. Defaults to False.

    Raises:
        ValueError: nNodes and nSums are invalid

    Returns:
        adjacency_list (list[list]) : Generated maps
    """
    
    # Validate
    if nEdges > nNodes * (nNodes - 1) // 2 and not isDirected:
        raise ValueError("Invlaid Values")
    if nEdges > nNodes * (nNodes - 1) and isDirected:
        raise ValueError("Invlaid Values")
    if nNodes <=0 or nEdges < 0:
        raise ValueError("Invlaid Values")

    # Init
    adjacency_list = [[] for _ in range(nNodes)]
    added_edges = set()
    
    # Generation
    while len(added_edges) < nEdges:
        
        u, v = random.sample(range(nNodes), 2)
        
        edge = (u, v)
        if not isDirected and u > v:
            edge = (v, u)
            
        if edge in added_edges:
            continue
        added_edges.add(edge)
        
        adjacency_list[u].append(v)
        if not isDirected:
            adjacency_list[v].append(u)
        
    return adjacency_list