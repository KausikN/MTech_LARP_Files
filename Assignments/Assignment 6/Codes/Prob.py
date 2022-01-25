'''
Probability Codes
'''

# Imports

# Main Functions
def SumCombinations(n, allowed_vals=[1, 2, 3, 4, 5, 6], max_len=3):
    '''
    All combinations of numbers summing up to n
    '''
    if max_len <= 1:
        return []
    # Initialize
    combinations = []
    # Loop through all numbers
    for i in allowed_vals:
        rem = n - i
        if rem in allowed_vals:
            combinations.append([i, rem])
        if rem > min(allowed_vals):
            subCombinations = SumCombinations(rem, allowed_vals, max_len-1)
            for subComb in subCombinations:
                combinations.append([i] + subComb)
    
    return combinations
    

# Driver Code
# Params
n = 12
# Params

# RunCode
combinations = SumCombinations(n, allowed_vals=[1, 2, 3, 4, 5, 6], max_len=3)

combinations_3 = []
for comb in combinations:
    if len(comb) == 3:
        combinations_3.append(comb)

print(len(combinations_3))
print(combinations_3)