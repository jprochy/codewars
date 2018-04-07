def spiralize(size):
    n = size + 4
    spiral = [ [0] * n for _ in range(n)]
    for j in range(size+4):
        spiral[1][j] = -1
        spiral[n-1][j] = -1
        spiral[j][1] = -1
        spiral[j][n-1] = -1
        spiral[0][j] = -1
        spiral[n-2][j] = -1
        spiral[j][0] = -1
        spiral[j][n-2] = -1
    pos = [2,2]
    a = pos[0]
    b = pos[1]
    spiral[a][b] = 1
    while (pos != [-1,-1]):
        if (spiral[a][b+2] <= 0) and (spiral[a][b+1] == 0): 
            while ((spiral[a][b+2] <= 0) and (spiral[a][b+1] == 0)):
                spiral[a][b+1] = 1
                pos = [a,b+1]
                a = pos[0]
                b = pos[1]
                
        elif (spiral[a+2][b] <= 0) and (spiral[a+1][b] == 0): 
            while ((spiral[a+2][b] <= 0) and (spiral[a+1][b] == 0)):
                spiral[a+1][b] = 1
                pos = [a+1,b]
                a = pos[0]
                b = pos[1]
        elif (spiral[a][b-2] <= 0) and (spiral[a][b-1] == 0): 
            while ((spiral[a][b-2] <= 0) and (spiral[a][b-1] == 0)):
                spiral[a][b-1] = 1
                pos = [a,b-1]
                a = pos[0]
                b = pos[1]
        elif (spiral[a-2][b] <= 0) and (spiral[a-1][b] == 0): 
            while ((spiral[a-2][b] <= 0) and (spiral[a-1][b] == 0)):
                spiral[a-1][b] = 1
                pos = [a-1,b]
                a = pos[0]
                b = pos[1]
        else:
            sum = 0
            if (spiral[a+1][b+1] == 1): sum+=1
            if (spiral[a+1][b] == 1): sum+=1
            if (spiral[a][b+1] == 1): sum+=1
            if (spiral[a-1][b-1] == 1): sum+=1
            if (spiral[a-1][b] == 1): sum+=1
            if (spiral[a][b-1] == 1): sum+=1
            if (spiral[a+1][b-1] == 1): sum+=1
            if (spiral[a-1][b+1] == 1): sum+=1
            print(sum)
            if (sum > 2): spiral[a][b] = 0
            pos = [-1,-1]
            

        
    
    
    
    
    
    spiral[:] = spiral[2:-2]
    for line in spiral:
        line[:] = line[2:-2]
        
    for i in range(n):
        print(spiral[i])   
    return spiral
    
spiralize(2)