def validate_move(listA, listB):
    if not listA:
        listA.append(listB.pop())
    elif not listB:
        listB.append(listA.pop())
    else:
        if listB[-1] > listA[-1]:
            listB.append(listA.pop())
        else:
            listA.append(listB.pop())    

def hanoi_solver(n: int) -> str:
    if not isinstance(n,int):
        raise   TypeError('Argument must be a integer')
    if n <= 1:
        raise ValueError("Number of disks must be higher than 1")
    moves = 2**n - 1
    left = [x for x in range(n,0,-1)]
    middle = []
    right = [] 
    index = 1
    path = f'{left} {middle} {right}'                   
    while index <= moves:       
        if n % 2 != 0:
            if index % 3 == 1:
                #Left and Right
                #check what's the valid move between 2 
                #make the move
                validate_move(left,right)                
            elif index % 3 == 2:
                #Left and Middle
                #check what's the valid move between 2 
                #make the move
                validate_move(left,middle)            
            else:
                #Middle and right
                #check what's the valid move between 2 
                #make the move
                validate_move(middle,right)                
        else:
            if index % 3 == 1:
                #Left and Middle
                #check what's the valid move between 2 
                #make the move
                validate_move(middle,left)           
            elif index % 3 == 2:
                #Left and Right
                #check what's the valid move between 2 
                #make the move
                validate_move(left,right)           
            else:
                #Middle and right
                #check what's the valid move between 2 
                #make the move
                validate_move(middle,right)
                                        
        path += f'\n{left} {middle} {right}'
        index += 1
    return path
print(hanoi_solver(5))