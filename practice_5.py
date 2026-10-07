# Given num and target ,return indicate [i,j](i,j) with num[i]+num[j]=target.and
# return [-1,-1] if there is None. 10^5 ,so aim for 0 n.
def two_sum(nums,target):
    seen={}

    for i,num in enumerate(nums):
        need=target-num
        if need in seen:
            return[seen[need],i]
        seen[num]=i
        return [-1,-1]