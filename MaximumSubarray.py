nums = [-2,1,-3,4,-1,2,1,-5,4]
currMax = float("-inf")
Max=0
for num in nums:
    currMax = max(num,currMax+num)
    Max = max(Max,currMax)
print(Max)
