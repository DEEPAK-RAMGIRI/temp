n = 3
m = 7
# recursion
def no_of_unique_paths(i,j):
    if i == 0 and j == 0: return 1
    elif i<0 or j <0: return 0
    up =no_of_unique_paths(i-1,j)
    left = no_of_unique_paths(i,j-1)
    return up + left
# print(no_of_unique_paths(n-1,m-1))    

# memoization
dp = [ [-1 for _ in range(m)] for _ in range(n)]
def no_of_unique_paths(i,j):
    if i == 0 and j == 0:
        return 1
    elif i < 0 or j< 0:
        return 0
    elif dp[i][j] != -1: return dp[i][j] 
    up = no_of_unique_paths(i-1,j)
    left = no_of_unique_paths(i,j-1)
    dp[i][j] = up + left
    return dp[i][j]
# print(no_of_unique_paths(n-1,m-1))

#tabulation

dp = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = 1
        else:
            up = dp[i-1][j] if i > 0 else 0
            left = dp[i][j - 1] if j > 0 else 0
            dp[i][j] = left + up
        
# print(dp[n-1][m-1])
