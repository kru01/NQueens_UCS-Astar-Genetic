from searchAlgo import *
import sys
import time
import tracemalloc

def main():
    numQueens, algo = [int(x) for x in input("Input queens and algo: ").split()]
    if numQueens < 0: numQueens = 0
    while numQueens > 500: numQueens = input("Over 500 queens is not a very good idea! Reinput queens: ")
    if algo < 1: algo = 1
    elif algo > 3: algo = 3

    problem = NQueens(numQueens)
    t0 = t1 = peakMemory = solution = 0
    if algo == 1:
        t0 = time.monotonic_ns()
        tracemalloc.start()
        solution = uniformCostSearch(problem).getSolution()
        peakMemory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        t1 = time.monotonic_ns()
        print(f'--{numQueens} Queens UCS--')
    elif algo == 2:
        t0 = time.monotonic_ns()
        tracemalloc.start()
        solution = AstartSearch(problem).getSolution()
        peakMemory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        t1 = time.monotonic_ns()
        print(f'--{numQueens} Queens A*--')
    elif algo == 3:
        chromDisplay = bool(int(input("Display chromosome? (0 for no): ")))
        problem = NQueensGenetic(numQueens, chromDisplay)
        t0 = time.monotonic_ns()
        tracemalloc.start()
        solution = handleGeneticAlgo(problem)
        peakMemory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        t1 = time.monotonic_ns()
        print(f'--{numQueens} Queens Genetic Algorithm--')
        print(f'Solved in Generation {problem.generation - 1}')
    
    print(f'Execution time: {(t1 - t0) / 10**6:15.4f} ms')
    print(f'Memory usage:   {peakMemory / 10**6:15.4f} MB')
    print(f'Solution: {solution}\n')
    problem.drawBoard(solution)
    sys.exit(0)

if __name__ == "__main__":
    main()