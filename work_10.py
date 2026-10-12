def rotate_Array(numbers,k):
    if not numbers:
        return []
    k=k%len(numbers)
    if k==0:
        return numbers
    last_k=numbers[-k:]
    remaining=numbers[:-k]
    result=last_k+remaining
    return result

print(rotate_Array([1,2,3,4,5],2))




        



        
