from graphs.graph import Graph, Vertex
from collections import deque

def dfs(grid, start_pos, visited):
    """
    Helper function for topological_sort
    """
    stack = deque()

    stack.append(start_pos)

    while len(stack) > 0:
        temp = stack.pop()
        if temp[0]+1 < len(grid):
            if grid[temp[0]+1][temp[1]] == 1:
                visited.add((temp[0]+1,temp[1]))
                stack.append((temp[0]+1,temp[1]))

        if temp[1]+1 < len(grid[0]):
            if grid[temp[0]][temp[1]+1] == 1:
                visited.add((temp[0],temp[1]+1))
                stack.append((temp[0],temp[1]+1))

    return visited

def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    num_islands = 0
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) not in visited and grid[i][j] == 1:
                num_islands += 1
                visited.add((i,j))
                visited = dfs(grid, (i,j), visited)

    return num_islands
# Test Cases
map1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
assert numIslands(map1) == 1

map2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
assert numIslands(map2) == 3


def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    num_of_oranges = 0
    counter = 0
    queue = deque()

    for row in grid:
        for elm in row:
            if elm == 1:
                num_of_oranges += 1
    if num_of_oranges == 0:
        return 0

    while num_of_oranges > 0:
        counter += 1
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 2:
                    if i-1 >= 0:
                        queue.append((i-1,j))
                    if j-1 >= 0:
                        queue.append((i,j-1))
                    if i+1 < len(grid):
                        queue.append((i+1,j))
                    if j+1 < len(grid):
                        queue.append((i,j+1))


        changes = 0
        while len(queue) > 0:
            temp = queue.popleft()
            if grid[temp[0]][temp[1]] == 1:
                num_of_oranges -= 1
                grid[temp[0]][temp[1]] = 2
                changes += 1

        if changes == 0:
            return -1

    return counter



# Test Cases
oranges1 = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
assert timeToRot(oranges1) == 4

oranges2 = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
assert timeToRot(oranges2) == -1

oranges3 = [
    [0,2]
]
assert timeToRot(oranges3) == 0


def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""
    graph = Graph(is_directed=True)

    for i in range(numCourses):
        graph.add_vertex(i)

    for elm in prerequisites:
        graph.add_edge(elm[1], elm[0])

    return graph.topological_sort()

# Test Cases
courses1 = [ [1,0] ]
assert courseOrder(2, courses1) == [0, 1]

courses2 = [ [1,0], [2,0], [3,1], [3,2] ]
possibleSchedules = [ [0, 1, 2, 3], [0, 2, 1, 3] ]
assert courseOrder(4, courses2) in possibleSchedules


def wordLadderLength(beginWord, endWord, wordList):
    """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""
    queue = deque()
    visited = set()
    word_path = dict()

    queue.append(beginWord)
    word_path[beginWord] = list()


    while len(queue) > 0:
        temp = queue.popleft()
        visited.add(temp)

        for word in wordList:
            if len(word) == len(temp):
                differences = 0
                for i in range(len(word)):
                    if word[i] != temp[i]:
                        differences += 1
                if differences == 1:
                    if word not in visited:
                        queue.append(word)
                    word_path[word] = word_path[temp] + [word]
                    if word == endWord:
                        return len(word_path[endWord])+1

    return -1

# Test Cases
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

assert wordLadderLength(beginWord, endWord, wordList) == 5
