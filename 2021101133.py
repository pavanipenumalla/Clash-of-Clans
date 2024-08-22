import copy

def VI(grid):
    count = 0
    do = 1
    discount = 0.95
    cost = -0.04
    while (True):
        if(do==0):
            policy = []
            new = []
            for i in range (4):
                for j in range (3):
                    new.append('x')
                policy.append(new)
                new = []
            for i in range(4):
                for j in range(3):
                    if grid[i][j]=='wall' or grid[i][j] == 1 or grid[i][j] == -1:
                        policy[i][j] = 'x'
                    else:
                        b = []
                        if (i-1>=0 and grid[i-1][j]!='wall'):
                            b.append(grid[i-1][j])  #north
                        if (i+1<=3 and grid[i+1][j]!= 'wall'):
                            b.append(grid[i+1][j]) #south
                        if (j-1>=0 and grid[i][j-1]!='wall'):
                            b.append(grid[i][j-1]) #west
                        if (j+1<=2 and grid[i][j+1]!='wall'):
                            b.append(grid[i][j+1]) #east
                        m = max(b)
                        if (i-1>=0 and grid[i-1][j]==m):
                            policy[i][j] ='^' #north
                        if (i+1<=3 and grid[i+1][j] == m ):
                            policy[i][j] ='south' #south
                        if (j-1>=0 and grid[i][j-1] ==m):
                            policy[i][j] = '<'#west
                        if (j+1<=2 and grid[i][j+1] == m):
                            policy[i][j] = '>' #east
            print("policy :")
            for p in policy:
                print(p)         
            break
        grid_old = copy.deepcopy(grid)   
        for i in range(4):
            for j in range(3):
                # print(i,j)
                if(grid_old[i][j]!= 'wall' and grid_old[i][j]!= 1 and grid_old[i][j]!= -1):
                # 4 actions possible - EAST , WEST , NORTH , SOUTH
                    actions = ['EAST', 'WEST', 'NORTH', 'SOUTH']
                    #action = east
                    a = []   
                    for action in actions:
                        if action == 'EAST':
                            if j+1 <= 2 and grid_old[i][j+1]!='wall':
                                a1 = 0.7 * grid_old[i][j+1]
                            else:
                                a1 = 0.7 * grid_old[i][j]
                        if action == 'NORTH' :
                            if i-1 >= 0 and grid_old[i-1][j]!='wall':
                                a2 = 0.15 * grid_old[i-1][j]
                            else:
                                a2 = 0.15 * grid_old[i][j]
                        if action == 'SOUTH' :
                            if i+1 <= 3 and grid_old[i+1][j]!='wall':
                                a3 = 0.15 * grid_old[i+1][j]
                            else:
                                a3 = 0.15 * grid_old[i][j]
                    x = a1+a2+a3
                    y = cost + (discount * x)
                    a.append(y)

                    #action = west
                    # x = 0
                    for action in actions:
                        if action == 'WEST':
                            if j-1 >=0 and grid_old[i][j-1]!='wall':
                                a1 = 0.7 * grid_old[i][j-1]
                            else:
                                a1 = 0.7 * grid_old[i][j]
                        if action == 'NORTH' :
                            if i-1 >= 0 and grid_old[i-1][j]!='wall':
                                a2 = 0.15 * grid_old[i-1][j]
                            else:
                                a2 = 0.15 * grid_old[i][j]
                        if action == 'SOUTH' :
                            if i+1 <= 3 and grid_old[i+1][j]!='wall':
                                a3 = 0.15 * grid_old[i+1][j]
                            else:
                                a3 = 0.15 * grid_old[i][j]
                    x = a1+a2+a3
                    y = cost + (discount * x)
                    a.append(y)

                    #action = north
                    x = 0
                    for action in actions:
                        if action == 'WEST':
                            if j-1 >=0 and grid_old[i][j-1]!='wall':
                                a1 = 0.15 * grid_old[i][j-1]
                            else:
                                a1 = 0.15 * grid_old[i][j]
                        if action == 'NORTH' :
                            if i-1 >= 0 and grid_old[i-1][j]!='wall':
                                a2 = 0.7 * grid_old[i-1][j]
                            else:
                                a2 = 0.7 * grid_old[i][j]
                        if action == 'EAST':
                            if j+1 <= 2 and grid_old[i][j+1]!='wall':
                                a3 = 0.15 * grid_old[i][j+1]
                            else:
                                a3 = 0.15 * grid_old[i][j]
                    x = a1+a2+a3
                    y = cost + (discount * x)
                    a.append(y)
                    
                    #action = south
                    # x = 0
                    for action in actions:
                        if action == 'WEST' :
                            if j-1 >=0 and grid_old[i][j-1]!='wall':
                                a1 = 0.15 * grid_old[i][j-1]
                            else:
                                a1 = 0.15 * grid_old[i][j]
                        if action == 'SOUTH' :
                            if i+1 <= 3 and grid_old[i+1][j]!='wall':
                                a2 = 0.7 * grid_old[i+1][j]
                            else:
                                a2 = 0.7 * grid_old[i][j]
                        if action == 'EAST' :
                            if j+1 <= 2 and grid_old[i][j+1]!='wall': 
                                a3 = 0.15 * grid_old[i][j+1]
                            else:
                                a3 = 0.15 * grid_old[i][j]
                    x = a1+a2+a3
                    y = cost + (discount * x)
                    a.append(y)
                     
                    grid[i][j] = max(a)         
        count +=1
        do = 0
        print("Iteration",count)
        for utility in grid:
            print(utility)
        for i in range(4):
            for j in range(3):
                if(grid_old[i][j] != 'wall'):
                    # print(abs(grid_old[i][j]-grid[i][j]))
                    if(abs(grid_old[i][j]-grid[i][j]) <= 0.0001):
                        do = 0
                    else:
                        do = 1
                        break
            if (do==1):
                break

        # print("do",do)
    return count
                    
grid = [[0, 1, -1], [0, 0, 0], [0, 'wall', 0], [0, 0, 0]]
count = VI(grid)
# print(count)