# def angram():
#     words=['eat','tea','tan','ate','nat','bat']

#     groups={}

#     for word in words:
#         key=tuple(sorted(word))

#         if key in groups:
#             groups[key].append(word)

#         else:
#             groups[key]=[word]
         

#     return list(groups.values())

# print(angram())


# 10. Maximum Subarray Sum (Kadane's algorithm)
# [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6
# Edge case: all negative numbers.

def max_subarray(nums):
    current_sum=nums[0]
    max_sum=nums[0]

    for num in nums[1:]:
        current_sum=max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)

    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_subarray(nums))