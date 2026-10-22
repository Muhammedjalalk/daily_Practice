def is_palidrome(s):
    s=s.lower()
    cleaned=""
    for char in s:
        if char.isalnum():
            cleaned+=char 
    return cleaned==cleaned[::-1]

print(is_palidrome("madam"))


#Count Vowels,Consonants,digts and  space
def Count_Charcter(s):
    vowels=0
    Consonents=0
    digit=0
    space=0

    for char in s.lower():
        if char in "aeiou":
            vowels+=1
        elif char not in "aeiou" and char.isalpha():
            Consonents+=1
        elif char.isdigit():
            digit+=1
        elif char==" ":
            space+=1
    return vowels,Consonents,digit,space

print(Count_Charcter("Today date is 2025"))