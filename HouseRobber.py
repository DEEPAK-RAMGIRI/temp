nums = [1,2,3,1]

# recursion
def rob_house(index):
    if index < 0: return 0
    consecutive = nums[index] + rob_house(index-2)
    no_consecutive = rob_house(index - 1)
    return max(consecutive,no_consecutive)
# print(rob_house(len(nums)-1))

# memoization
dp = [-1] * len(nums)
def rob_house(index):
    if index < 0: 
        return 0
    elif dp[index] != -1:
        return dp[index]
    consecutive = nums[index] + rob_house(index-2)
    no_consecutive = rob_house(index - 1)
    dp[index] = max(consecutive,no_consecutive)
    return  dp[index]
# print(rob_house(len(nums)-1))
    
    
# tabulation
dp = [-1] * (len(nums))
dp[0] = nums[0]
dp[1] = max(nums[0],nums[1])
for i in range(2,(len(nums))):
    dp[i] = max(dp[i -2] + nums[i],dp[i-1])
# print(dp)
# print(dp[len(nums)-1])
