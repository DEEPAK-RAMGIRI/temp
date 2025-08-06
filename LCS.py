text1 = "abcde"
text2 = "ace" 

# Recursion
def longest_common_subsequence(i,j):
    
    if i < 0 or j < 0: return 0
    elif text1[i] == text2[j]: return 1 + longest_common_subsequence(i-1,j-1)
    else: return max(longest_common_subsequence(i-1,j),longest_common_subsequence(i,j-1))
    
# print(longest_common_subsequence(len(text1)-1,len(text2)-1))

# memoization
dp = [[-1 for _ in range(len(text1))] for _ in range(len(text2))]
def longest_common_subsequence(i,j):
    if i < 0 or j < 0: return 0
    elif dp[i][j] != -1: 
        return dp[i][j]
    elif text2[i] == text1[j]: return 1 + longest_common_subsequence(i-1,j-1)

    from_left_side = longest_common_subsequence(i,j-1)
    from_top_side = longest_common_subsequence(i-1,j)
    dp[i][j] = max(from_left_side,from_top_side)
    return dp[i][j]
# print(longest_common_subsequence(len(text2)-1,len(text1)-1))

#tabulation
dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
for i in range(len(text1)):
    for j in range(len(text2)):
        
        if text1[i] == text2[j]:
            if i > 0 and j > 0:
                dp[i][j] = 1 + dp[i - 1][j -1]
            else:
                dp[i][j] = 1 
        else:
            left_side = dp[i][j-1] if j > 0  else 0
            top_side = dp[i-1][j] if i > 0 else 0
            dp[i][j] = max(left_side,top_side) 
            
# print(dp[len(text1)-1][len(text2)-1
