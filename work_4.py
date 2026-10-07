def first_duplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return None

num=[4,2,7,5,2,8,7,2]
print(first_duplicate(num))





