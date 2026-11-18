# Remove Duplicate character while keeping the original order
def remove_duplicate(s):
    result=[]
    seen=set()

    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)

    return "".join(result)

print(remove_duplicate("programming"))

        
