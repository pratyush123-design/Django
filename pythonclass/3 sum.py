
nums = [-2, -1, 0, 1, 2, 3, 4]
nums.sort()

i = 0 

while i < len(nums) - 2: 
    j = i + 1  
    k = len(nums) - 1 

    
    if i > 0 and nums[i] == nums[i - 1]:
        i += 1
        continue  

    while j < k:
        
        if nums[i] + nums[j] + nums[k] == 0:
            print(f"Triplet found: {nums[i]}, {nums[j]}, {nums[k]}")
            
           
            j += 1
            k -= 1
            
            # while j < k and nums[j] == nums[j - 1]:
            #     j += 1
            
            # while j < k and nums[k] == nums[k + 1]:
            #     k -= 1
        
       
        elif nums[i] + nums[j] + nums[k] < 0:
            j += 1
        
   
        else:
            k -= 1

  
    i += 1
    while i < len(nums) - 2 and nums[i] == nums[i - 1]:
        i += 1  

print("Sorted nums:", nums)
