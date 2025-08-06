
# Recursion
string = '226' 
def decodeways(index):
    if index == len(string): return 1
    elif string[index] == "0":return 0
    total = decodeways(index + 1)
    if index + 2 < len(string) and 10 <= int(string[index:  index + 2]) <= 26:
        total += decodeways(index + 2)
    return total 
# print(decodeways(0))

# memoization
dp = [-1] * len(string)
def decodeways(index):
    if index == len(string): return 1
    elif string[index] == '0':return 0
    elif dp[index] != -1:
        return dp[index]
    dp[index] = decodeways(index + 1)
    if index + 1 < len(string) and 10 <= int(string[index : index + 2]) <= 26:
        dp[index] += decodeways(index + 2)
    return dp[index]
# print(decodeways(0))

# tabulation
dp = [-1] * (len(string) + 1)
dp[-1] = 1
for i in range(len(string)-1,-1,-1):
    if string[i] == '0': dp[i] = 0
    else:
        dp[i] = dp[i+1]
        if i + 1 < len(string) and  10 <= int(string[i :i + 2]) <= 26:
            dp[i] += dp[i + 2]
print(dp[0])
