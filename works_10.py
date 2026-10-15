def addBinary(a,b):
    carry=0
    result=""

    while a or b or carry:
        if a:
            last_digit=int(a[-1])
            a=a[:-1]
        else:
            last_digit=0
        if b:
            second_last=int(b[-1])
            b=b[:-1]
        else:
            second_last=0

        total=last_digit+second_last+carry

        digit=total%2
        carry=total//2

        result=str(digit)+result
    return result

print(addBinary("101","110"))


    


        