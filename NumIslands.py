# https://www.geeksforgeeks.org/find-number-of-islands/

islands = [[1, 1, 0, 0, 0], # --> j
           [0, 1, 0, 0, 1],
           [1, 0, 0, 1, 1],
           [0, 0, 0, 0, 0],
           [1, 0, 1, 0, 1]]

print("Input island")
for row in islands:
  print(row)


def isValidIndex(m, n, i, j):
  if i < m and i >= 0 and j < n and j >= 0:
    return True
  else:
    return False

def neighborsOf(islandsIn, i0, j0):
  """
  neighbors
  i - 1, j - 1
  i - 1, j
  i    , j - 1
  i + 1, j + 1
  i + 1, j
  i    , j + 1
  i - 1, j + 1
  i + 1, j - 1
  """
  validNeighbors = []
  iIdx = [-1, -1, 0, 1, 1, 0, -1, 1]
  jIdx = [-1,  0,-1, 1, 0, 1,  1, -1]

  m = len(islandsIn)
  n = len(islandsIn[0])

  for k in range(8):      
      if isValidIndex(m, n, i0 + iIdx[k], j0 + jIdx[k]):
        validNeighbors.append([i0 + iIdx[k], j0 + jIdx[k]])

  return validNeighbors



def dfs2D(islandsIn, i0, j0):

  # print(islandsIn)
  if islandsIn[i0][j0] == 1:
    islandsIn[i0][j0] = -1
    # print(islandsIn)

    for [i, j] in neighborsOf(islandsIn, i0, j0):    
      
      if islandsIn[i][j]== 1:
        dfs2D(islands, i, j)



countIsland = 0

for i in range(len(islands)):
  for j in range(len(islands[0])):
    if islands[i][j] == 1:
      countIsland += 1
      dfs2D(islands, i, j)


print("Num Islands DFS: ", countIsland)


# BFS 

islands = [[1, 1, 0, 0, 0], # --> j
           [0, 1, 0, 0, 1],
           [1, 0, 0, 1, 1],
           [0, 0, 0, 0, 0],
           [1, 0, 1, 0, 1]]

def bfs2D(islandsIn, i0, j0):
    q = []
    q.append([i0, j0])

    while q:
      curr_i, curr_j = q.pop(0)
      islandsIn[curr_i][curr_j] = -1

      for [i, j] in neighborsOf(islandsIn, curr_i, curr_j):
        if islandsIn[i][j] == 1:          
          q.append([i, j])

countIslandBFS = 0

for i in range(len(islands)):
  for j in range(len(islands[0])):
    if islands[i][j] == 1:
      countIslandBFS += 1
      bfs2D(islands, i, j)


print("Num Islands BFS: ", countIslandBFS)