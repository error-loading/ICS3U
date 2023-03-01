# # lists
# # A list is a variable that can hold multile values
# # These values can be of any type, even lists.
# nums = [12, 5, 6, 23]
# print(nums[0])   # not a list (int)

# print(nums[1:3])
# nums[1] = 99 # NEW - you can assign to slices
# print(nums)

# nums[2:3] = [1,2,3,4]    # This is not used very often
# print(nums)

# # multiply lists
# rain = [0] * 7
# print(rain)

# # add lists
# rain = rain + [1, 1, 1, 1]
# print(rain)

# # Add and remove elements
# # Add - append
# nums = [0]
# nums.append(89)
# print(nums)

# # nums = nums + [89]   - slower
# # nums = [89] + nums
# nums.insert(0, 22)  # can insert anywhere 
# print(nums)

nums = [12, 5, 99, 6, 23, 99]
# remove based value
nums.remove(99)    # removes ONLY the first occurence
print(nums)
# remove based on position
del nums[0]
print(nums)

print(nums.count(99))

if 6 in nums:
    print(nums.index(6))    # Gives you the position of a value in the list, and kindly crashes if not there

print(len(nums))
print(sum(nums))
print(min(nums))
print(max(nums))

for n in nums:
    print(n)

animals = ["dog", "cat", "rat", "elk", "bad", "bee"]
animals.sort()
print(animals)

animals.reverse()
animal = animals.pop()
print(animal)
print(animals)