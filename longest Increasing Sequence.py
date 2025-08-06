# generate subsequence with the given array
arr = [10,9,2,5,3,7,101,18]
ans = []
def generate_subsequence(index,temp):
    if index  == len(arr):
        ans.append(temp[:])
        return
    
    generate_subsequence(index + 1,temp)
    
    if not temp or temp[-1] < arr[index]:
        temp.append(arr[index])
        generate_subsequence(index + 1,temp)
        temp.pop()
    
    
# generate_subsequence(0,[])
# print(ans)  

#  Longest Increasing Subsequence

# recursion   
def generate_subsequence(index,prev):
    if index == len(arr):
        return 0
    with_ = generate_subsequence(index+1,prev)
    with_out = 0
    if prev == -1 or arr[prev] < arr[index]:
        with_out  = 1  + generate_subsequence(index+1,index)
    return max(with_ ,  with_out)
print(generate_subsequence(0,-1))

# Memoization
dp = [[-1 for _ in range(len(arr) + 1)] for i in range(len(arr))]

def generate_subsequence(index,prev_index):
    if index == len(arr): return 0
    elif dp[index][prev_index + 1] != -1: return dp[index][prev_index + 1]
    with_ = generate_subsequence(index + 1,prev_index)
    with_out = 0
    if prev_index == -1 or arr[prev_index] < arr[index]:
        with_out  = 1 + generate_subsequence(index + 1,index)
    dp[index][prev_index] = max(with_,with_out)
    return dp[index][prev_index]
# print(generate_subsequence(0,-1))

# Tabulation
dp = [1] * len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j] + 1)
# print(max(dp))  
