import random

class NQueens:
    def __init__(self, numQueens, isIncremental=True) -> None:
        self.numQueens = numQueens
        self.isIncremental = isIncremental
        if isIncremental: self.initState = (-1,) * numQueens
        else: self.initState = tuple([random.randrange(0, numQueens) for _ in range(numQueens)])

    def checkConfict(self, r1, c1, r2, c2) -> bool:
        return r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2)
    
    def goalTest(self, state) -> bool:
        if self.isIncremental:
            try:
                if state[-1] == -1: return False
            except IndexError: return True

        for c1, r1 in enumerate(state):
            for c2, r2 in enumerate(state):
                if (r1, c1) != (r2, c2) and self.checkConfict(r1, c1, r2, c2):
                    return False                
        return True
    
    def getActions(self, state) -> list:
        if self.isIncremental:
            if state[-1] != -1: return []
            validActions = list(range(self.numQueens))
            currCol = state.index(-1)
            for currRow in range(self.numQueens):
                for c, r in enumerate(state[:currCol]):
                    if currRow in validActions and self.checkConfict(currRow, currCol, r, c):
                        validActions.remove(currRow)
            return validActions
        
        validActions = []
        for currCol in range(self.numQueens):
            for currRow in range(self.numQueens):
                if currRow != state[currCol]: validActions.append((currRow, currCol))
        return validActions
    
    def placeQueen(self, state, action) -> tuple:
        if self.isIncremental:
            col = state.index(-1)
            newState = list(state[:])
            newState[col] = action
            return tuple(newState)
        
        newState = list(state)
        newState[action[1]] = action[0]
        return tuple(newState)
    
    def calcPathCost(self, cost) -> int:
        return cost + 1
    
    def calcHeuristic(self, state) -> int:
        conflicts = 0
        for c1, r1 in enumerate(state):
            for c2, r2 in enumerate(state[c1 + 1:], c1 + 1):
                if self.checkConfict(r1, c1, r2, c2): conflicts += 2
        return conflicts
    
    def drawBoard(self, board) -> None:
        if not board: return
        print("      ", end="")
        for col in range(len(board)): print("%3d " % col, end="")
        separator = '-' * (len(board) * 4 + 2)
        print("\n     " + separator)

        for row in range(len(board)):
            print("%3d | " % row, end="")
            for col in range(len(board)):
                if board[col] == row: print("  Q ", end="")
                else: print("  * ", end="")
            print(" | ", row)

        print("     " + separator + "\n      ", end="")
        for col in range(len(board)): print("%3d " % col, end="")
        print("")
        
class Node:
    def __init__(self, state, parent=None, action=None, pathCost=0, heuristic=0) -> None:
        self.state = state
        self.parent = parent
        self.action = action
        self.pathCost = pathCost
        self.heuristic = heuristic
        self.depth = 0
        if parent: self.depth = parent.depth + 1
    
    def getChildNode(self, problem, action):
        pass

    def expand(self, problem) -> list:
        return [self.getChildNode(problem, action) for action in problem.getActions(self.state)]
    
    def __lt__(self, node):
        pass

class NodeUCS(Node):
    def __init__(self, state, parent=None, action=None, pathCost=0) -> None:
        super().__init__(state, parent, action, pathCost)

    def getChildNode(self, problem, action):
        nextState = problem.placeQueen(self.state, action)
        nextNode = NodeUCS(nextState, self, action, problem.calcPathCost(self.pathCost))
        return nextNode
    
    def __lt__(self, node):
        return self.pathCost < node.pathCost
    
class NodeAstar(Node):
    def __init__(self, state, parent=None, action=None, pathCost=0, heuristic=0) -> None:
        super().__init__(state, parent, action, pathCost, heuristic)

    def getChildNode(self, problem, action):
        nextState = problem.placeQueen(self.state, action)
        nextNode = NodeAstar(nextState, self, action, problem.calcPathCost(self.pathCost), problem.calcHeuristic(nextState))
        return nextNode
    
    def __lt__(self, node):
        return (self.pathCost + self.heuristic) < (node.pathCost + node.heuristic)
    
class NQueensGenetic(NQueens):
    def __init__(self, numQueens, chromDisplay) -> None:
        super().__init__(numQueens)
        self.chromDisplay = chromDisplay
        self.maxConflicts = numQueens * (numQueens - 1) # nC2 * 2
        self.generation = 1
        self.population = [self.getRandomChromosome(numQueens) for _ in range(100)]

    def getRandomChromosome(self, size) -> list:
        return [random.randint(0, size - 1) for _ in range(size)]
    
    def calcFitness(self, chromosome) -> int:
        return self.calcHeuristic(chromosome)
    
    def calcProbability(self, chromosome) -> float:
        return self.calcFitness(chromosome) / self.maxConflicts
    
    def pickRandomly(self, population, probabilites) -> list:
        total = sum(prob for prob in probabilites)
        rand = random.uniform(0, total)
        cumulativeProb = 0
        for chrom, prob in zip(population, probabilites):
            cumulativeProb += prob
            if cumulativeProb >= rand: return chrom

    def reproduce(self, x, y) -> list:
        xLen = len(x)
        crossoverPoint = random.randint(0, xLen - 1)
        return x[0:crossoverPoint] + y[crossoverPoint:xLen]
    
    def mutate(self, x) -> list:
        xLen = len(x)
        randInd = random.randint(0, xLen - 1)
        randVal = random.randint(0, xLen - 1)
        x[randInd] = randVal
        return x
    
    def print_chromosome(self, chrom):
        print("Chromosome = {},  Fitness = {}".format(str(chrom), (self.calcFitness(chrom))))
        
    def geneticQueen(self, population):
        mutationProb = 0.8
        newPopulation = []
        probs = [self.calcProbability(chrom) for chrom in population]
        for _ in range(len(population)):
            #ch1 = self.pickRandomly(population, probs)
            #ch2 = self.pickRandomly(population, probs)
            ch1, ch2 = random.choices(population, weights=probs, k=2)
            child = self.reproduce(ch1, ch2)
            if random.random() < mutationProb: child = self.mutate(child)
            if self.chromDisplay: self.print_chromosome(child)
            newPopulation.append(child)
            if self.calcFitness(child) == 0: break
        return newPopulation
