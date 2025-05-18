
nums=list(map(int,input("Enter the number of list: ").split()))
Target=int(input("Enter the targetted number: "))
def twoSums(nums,Target):
    hash_map={}
    for i,num in enumerate (nums):
        if Target-num in hash_map:
            return[hash_map[Target-num],i]
        hash_map[num]=i
    return[]
print (twoSums(nums,Target))

print("Hello")


nums = list(map(int, input("Enter numbers separated by space: ").split()))
Target = int(input("Enter the targetted number: "))
def twoSumsAll(nums, Target):
    hash_map = {}
    result = []

    for i, num in enumerate(nums):
        complement = Target - num
        if complement in hash_map:
            result.append([hash_map[complement], i])
        hash_map[num] = i

    return result


print(twoSumsAll(nums, Target))




