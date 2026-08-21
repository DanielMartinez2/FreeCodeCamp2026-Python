def is_safe(mat,row,col):
    n = len(mat)    
    #checar se não tem nada acima na coluna
    for i in range(row):
        if(mat[i][col]):
            return False
    #checar diagonal principal
    i = row - 1
    j = col - 1
    while i>=0 and j>=0:
        if mat[i][j]:
            return False
        i-=1
        j-=1


    #Checar diagonal secundária
    i = row - 1
    j = col + 1
    while i>=0 and j<n:
        if mat[i][j]:
            return False
        i-=1
        j+=1
    return True

def place_queens(mat,row,result):
    n = len(mat)
    
    #caso base
    if (row == n):
        ans = []
        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    ans.append(j)
        result.append(ans)    
        return
    
    for i in range(n):
        if is_safe(mat,row,i):
            mat[row][i] = 1
            place_queens(mat, row+1, result)
            #backtrack
            mat[row][i] = 0
    




def dfs_n_queens(n: int) -> list:
    if not isinstance(n,int):
        raise TypeError("Must be an integer")
    if n < 1:
        return []    
    board = [[0]*n for _ in range(n)]       
    result = []
    place_queens(board, 0, result)    
    return result
