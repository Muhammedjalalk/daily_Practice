def unique_char(s):
    count={}

    for i,char in enumerate(s):
        count[char]=count.get(char,0)+1

    for i,char in enumerate(s):
        if count[char]==1:
            return i,char
    return -1
s="leetcode"
print(unique_char(s))


#find Sceond largest in a list

def second_largest(numbers):
    largest=float("-inf")
    second=float("-inf")

    for num in numbers:
            if num>largest:
                second=largest
                largest=num
            else:
                if num>second and num!=largest:
                    second=num
    return second           
numbers = [10, 5, 8, 10, 3, 8, 7]
print(second_largest(numbers))
    
            

        
    
