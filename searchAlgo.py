from NQueens import *
import heapq

def uniformCostSearch(problem : NQueens) -> Node:
    node = NodeUCS(problem.initState)
    return handleSearchSet(node, problem)

def AstartSearch(problem : NQueens) -> Node:
    node = NodeAstar(problem.initState, heuristic=problem.calcHeuristic(problem.initState))
    return handleSearch(node, problem)

def handleSearchSet(node: Node, problem: NQueens) -> Node:
    expanded = set()
    frontier = [node]
    heapq.heapify(frontier)
    expanded.add(problem.initState)
    while frontier:
        current = heapq.heappop(frontier)
        if problem.goalTest(current.state): return current
        children = current.expand(problem)
        for i in children:
            if i.state not in expanded:
                heapq.heappush(frontier, i)
                expanded.add(i.state)
    return Node((), None, None)

def handleSearch(node: Node, problem: NQueens) -> Node:
    frontier = [node]
    heapq.heapify(frontier)
    expanded = [problem.initState]
    while frontier:
        current = heapq.heappop(frontier)
        if problem.goalTest(current.state): return current
        if current in expanded: continue
        children = current.expand(problem)
        expanded.append(current)
        for i in children:
            if i not in expanded: heapq.heappush(frontier, i)
    return Node((), None, None)

def handleGeneticAlgo(problem : NQueensGenetic) -> list:
    if not problem.chromDisplay: print("The program is not actually stuck. Please wait...")
    while not 0 in [problem.calcFitness(chrom) for chrom in problem.population]:
        if problem.chromDisplay: print(f'== Generation {problem.generation} ==')
        problem.population = problem.geneticQueen(problem.population)
        problem.generation += 1
    for chrom in problem.population:
        if problem.calcFitness(chrom) == 0: return chrom