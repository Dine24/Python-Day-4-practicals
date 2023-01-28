def smallerNumbersThanCurrent(nums): 
  result = [] 
  for i in range(len(nums)): 
    count = 0 
    for j in range(len(nums)): 
      if i == j: 
        continue
      if nums[j] < nums[i]: 
        count += 1
    result.append(count) 
  return result 

print(smallerNumbersThanCurrent([8,1,2,2,3])) 
print(smallerNumbersThanCurrent([6,5,4,8]))
print(smallerNumbersThanCurrent([7,7,7,7]))
print(smallerNumbersThanCurrent([1,2,3,5,5,6]))
print(smallerNumbersThanCurrent([0,0,0,0]))
