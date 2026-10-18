def maxSlideWindow(nums,k):
    result=[]
    deque=[]
    for i in range(len(nums)):
        while deque!=[]  and deque[0]<=i-k:
           deque.pop(0)

        while deque!=[] and nums[deque[-1]]<nums[i]:
            deque.pop()
        deque.append(i)

        if i+1>=k:
            result.append(nums[deque[0]])
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(maxSlideWindow(nums, k))



