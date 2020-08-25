# from graphs.graph import Graph, Vertex
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

#
# def timeToRot(grid):
#     """
#     Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
#     orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
#     of minutes until all oranges rot.
#     """
#     pass
#
# # Test Cases
# oranges1 = [
#     [2,1,1],
#     [1,1,0],
#     [0,1,1]
# ]
# assert timeToRot(oranges1) == 4
#
# oranges2 = [
#     [2,1,1],
#     [0,1,1],
#     [1,0,1]
# ]
# assert timeToRot(oranges2) == -1
#
# oranges3 = [
#     [0,2]
# ]
# assert timeToRot(oranges3) == 0
#
#
# def courseOrder(numCourses, prerequisites):
#     """Return a course schedule according to the prerequisites provided."""
#     pass
#
# # Test Cases
# courses1 = [ [1,0] ]
# assert courseOrder(2, courses1) == [0, 1]
#
# courses2 = [ [1,0], [2,0], [3,1], [3,2] ]
# possibleSchedules = [ [0, 1, 2, 3], [0, 2, 1, 3] ]
# assert courseOrder(4, courses2) in possibleSchedules
#
#
# def wordLadderLength(beginWord, endWord, wordList):
#     """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""
#     pass
#
# # Test Cases
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# assert wordLadderLength(beginWord, endWord, wordList) ==
