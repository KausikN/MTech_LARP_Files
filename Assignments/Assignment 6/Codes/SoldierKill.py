'''
Soldiers Kill Problem
'''

# Imports

# Main Functions
def SoldiersKill(n):
    '''
    Soldier Kill Problem
    '''

    # Initialize
    soldiers = list(range(1, n + 1))
    alive = list(soldiers)
    killed = []

    # Loop
    it = 0
    while len(alive) > 1:
        print(it)
        print("ALIVE:", len(alive), alive)
        print("KILLED:", len(killed), killed)
        it += 1
        if len(alive) % 2 == 0:
            killed.extend(alive[1::2])
            alive = alive[::2]
        else:
            last_person = alive[-1]
            alive = alive[:-1]
            killed.extend(alive[1::2])
            killed.append(alive[0])
            alive = alive[::2] + [last_person]
            alive = alive[1:]

    return alive
    

# Driver Code
# Params
n = 41
# Params

# RunCode
alive = SoldiersKill(n)
print(alive)