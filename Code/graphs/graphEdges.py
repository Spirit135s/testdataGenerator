import random
import sys

def generate_random_edges(nNodes, nEdges, isDirected=False):
    """
    Generate a random Graph

    Args:
        nNodes (int): sum of Nodes
        nEdges (int): sum of Edges
        isDirected (bool, optional): Tell if then map is directed. Defaults to False.

    Raises:
        ValueError: nNodes and nSums are invalid

    Returns:
        edges (list) : Generated edges
    """
    
    if nEdges > nNodes * (nNodes - 1) // 2 and not isDirected:
        raise ValueError("Invalid Values")
    if nEdges > nNodes * (nNodes - 1) and isDirected:
        raise ValueError("Invalid Values")
    if nNodes <= 0 or nEdges < 0:
        raise ValueError("Invalid Values")
    
    edges = set()

    while len(edges) < nEdges:
        u, v = random.sample(range(nNodes), 2)
        edge = (u, v)
        if not isDirected and u > v:
            edge = (v, u)

        if edge in edges:
            continue
        edges.add(edge)

    if not isDirected:
        edges = list(edges)
    else:
        edges = [(u, v) for u, v in edges] + [(v, u) for u, v in edges]

    return list(edges)


if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) <= 2 or len(argvs) >= 5:
        print("Usage: generate_edges.py <nNodes> <nEdges> <isDirected (true/false(Default))>")
        sys.exit(1)

    nNodes = int(argvs[1])
    nEdges = int(argvs[2])
    if len(argvs) == 4:
        isDirected = argvs[3].strip().lower() == "true"
    else:
        isDirected = False

    try:
        edges = generate_random_edges(nNodes, nEdges, isDirected)
        print("Edges are as follows:")
        for edge in edges:
            print(f"{edge[0]} -> {edge[1]}")
    except ValueError as e:
        print(f"Error: {e}")