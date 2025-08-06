grid = [[1,3,1],[1,5,1],[4,2,1]]

# recursion
def find_min_sum(i,j):
    if i == 0 and j == 0:
        return grid[i][j]
    elif i < 0 or j < 0:
        return float("inf")
    upside = find_min_sum(i - 1,j)
    leftside = find_min_sum(i,j - 1)
    return min(upside,leftside) + grid[i][j]
# print(find_min_sum(len(grid)-1,len(grid[0])-1))

# memoization
dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
def find_min_sum(i,j):
    if i == 0 and j == 0:
        return grid[i][j]
    elif i < 0 or j < 0:
        return float("inf")
    elif dp[i][j] != -1:
        return dp[i][j]
    upside = find_min_sum(i - 1,j)
    leftside = find_min_sum(i,j - 1)
    dp[i][j] = min(upside,leftside) + grid[i][j]
    return dp[i][j]
# print(find_min_sum(len(grid)-1,len(grid[0])-1))

# tabulation
dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]
        else:
            upside = dp[i-1][j] if i > 0 else float("inf") 
            leftside = dp[i][j-1] if j > 0 else float("inf")
            dp[i][j] = min(upside,leftside) + grid[i][j]
print(dp[len(grid)-1][len(grid[0])-1])
