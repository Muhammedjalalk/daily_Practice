def  two_sum(nums,target):
    seen={}

    for i,num in enumerate(nums):
        needed=target-num
        seen[num]=i

        if needed in seen:
            return [seen[needed],i]

print(two_sum([2,7,11,15],9))


# Reverse a string "hello" Without using slicing
#Expected output "olleh"

def Revers_string(text):
    reverse=""
    for char in text:
        reverse=char+reverse

    return reverse

print(Revers_string("hello"))
    

 


    