#Reverse a string 

text="hello"
reverse=""
for char in text:
    reverse=char+reverse

print(reverse)


#check give string is palindrome
str="Mala  yalam"
str=str.lower()
str=str.replace(" ","")
reverse=''
for char in str:
    reverse=str[::-1]
if str==reverse:
     print("string is palidrome")
else:
    print("String not palidrome")


#Sample 3 logical operator sample Code
a=10
b=20
print(a > 7  and  b > 10)
print(a < 11 or b > 20)
print(a>10 or b<21)
print(not(a>10))



#Sample anonymous fuction Example code 
#normal
def add(a,b):
    return a+b

print(add(10,20))


#lambda fuction 

# anonymous fuction is a fuction without a name

add= lambda a,b:a+b
print(add(10,20))
multiple=lambda a,b:a*b
print(multiple(20,40))


# find the longest word Sentance in list

def longest_word(s):
    longest=""
    s=s.split()
    for word in s:
        if len(word)>len(longest):
            longest=word

    return longest

print(longest_word("Python is powerfull programming language"))



def capitalize(s):
    return s.title()

print(capitalize("hello world python"))


def reverse_word(s):
    words=s.split()
    reverse=""
    for word in words:
        reverse=word+reverse
    return reverse
print(reverse_word("python is a programming language"))

def reverse_word(s):
    words=s.split()
    words.reverse()
    reverse=" ".join(words)
    return reverse
   
print(reverse_word("this python program"))

