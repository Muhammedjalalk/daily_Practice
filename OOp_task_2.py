squares=[x*x for x in range(1,6)]
print(squares)


#Find Second largest number in a list
list1=[10,23,34,5,6,3,2,18,24,56]
largest=float('-inf')
second_largest=float('-inf')

for num in list1:
    if num>largest:
        second_largest=largest
        largest=num

    elif num>second_largest and num!=largest:
        second_largest=num 
print("Second Largest",second_largest)