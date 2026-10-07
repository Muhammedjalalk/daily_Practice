!
# x="apple"

# def changes(a):
#     a+= " is Fruits"
#     return a
# print(changes(x))
# print(x)

def find_second_largest(nums):
    if len(nums)<2:
        return None
    largest=second=float('-inf')
    for num in nums:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second=num

    if second==float('-inf'):
        return None
    return second
    
numbers=[10,20,30,40,50]
print(find_second_largest(numbers))



