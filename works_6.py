
#list
# fruits=["Apple","Banana","Apple"]
# fruits.append("Orange")
# print(fruits)

#Tuple
# corrdinates=(10,20)
# print(corrdinates[0])


#Fction is resuble black of code  that performing specfic task
# def greet():
#     print("Hello, Arun")

# greet()

# def add(a,b):
#     return a +b

# result=add(12,34)

# print(result)


#args and *kwargs they are used when we don't know in advance how many arguments a fuction will recive
# def add(*args):
#     print(args)
# add(10,20,30,40)


# def add(*args):
#     return sum(args)
# print(add(10,20,40,30))

#multi Keyword Arument 
# def Student(**kwargs):
#     print(kwargs)

# Student(name="Jalal",Age=21,Course="Computer Science")

#Reverse a string
string="hello Jalal"
reverse=""
for char in string:
    reverse=char+reverse

print(reverse)


#logest Substrin

def logest_substr(a):
    left=0
    right=0
    current_length=0
    seen=set()

    while(left<right):
        current_length=right-left+1
        
