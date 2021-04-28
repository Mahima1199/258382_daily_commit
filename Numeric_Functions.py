# Numeric functions used in a list
print(min(1,2,3,4,5))
print(max(1,2,3,4,5))
print(abs(-99))
print(abs(42))
print(sum([1,2,3,4,5]))

# some more functions in list
nums = [55,44,33,22,11]
if all([i>5 for i in nums]):
    print("All greater than 5")
if any([i%2==0 for i in nums]):
    print("At least one is even")
for v in enumerate(nums):
    print(v)
