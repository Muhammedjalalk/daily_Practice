def Check_anagrams(a,b):
    a=a.lower()
    b=b.lower()

    if sorted(a)==sorted(b):
        return "Anagrams"

    else:
        return "Not Anagrams"


print(Check_anagrams("Listen","silent"))

