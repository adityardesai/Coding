'''
Description
Assume there is a game. Given a 2D grid as a map, each cell is either a wall 2, a vampire 1 or people 0 (the number zero, one, two).Vampires can turn the nearest people(up/down/left/right) into vampire every day, but they can not through the walls. How long will it take to turn all people into vampires? Return -1 if can not turn all people into vampires.

Example 1:

people-0
wall-2
vampire-1

Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
 
 
Output:
2
'''

"""
    0 1 2 3 4
    
0   1,1,2,1,1
1   1,1,1,2,1
2   1,1,1,1,1
"""

from collection import deque


def _is_valid(matrix, r,c):
    
    if r<0 or c<0 or r>len(matrix)-1 or c>len(matrix[0])-1:
        return False
    return True


def vampireTime(matrix):
    
    if not matrix:
        # raise Exception # client can get proper message
        return -1
    
    r=len(matrix) # 3
    c=len(matrix[0]) # 4
    
    queue = deque() # [(0,1), (1,0), (1,4), (2,1)]
    count=0 # 0
    people=0 # 9
    directions=[(1,0),(-1,0),(0,1)(0,-1)]
    
    
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==1: # if its vampire
                 queue.append((i,j))
            elif matrix[i][j]==0:
                people+=1
    
    if people==0:
        return -1
    
    while queue:
        count+=1 # 1
        
        for i in range(len(queue)):  
            x,y = queue.popleft() # 
            for d in directions: # 
                n_x=x+d[0] # 0
                n_y=y+d[1] # 2
                if _is_valid(matrix, n_x, n_y) and matrix[n_x][n_y]==0:
                    people-=1
                    matrix[n_x][n_y]=1
                    queue.append((n_x,n_y))
    
    if people==0:
        return count
    else:
        return -1
