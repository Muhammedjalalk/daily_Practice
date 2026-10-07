
#Compersion bettween == and is
# a=[1,2,3]
# b=a
# print(a==b)
# print(a is b)

#programm to find different betwwen list and tuple
# fruits=['apple','banana','Orange',]
# fruits.append('mango')  #appned add elements to the list
# print("Fruits=",fruits)

#Programm for check tuple is mutable
# fruits=('apple','banana','Orange')
# fruits[0]='mango' #TypeError: 'tuple' object does not support item assignment

#Above Check in number cause 
# numbers=[12,34,56,67,45]
# numbers[2]=29
# print(numbers)


#Cause in Tuble
# numbers=(23,82,12,3)
# numbers[2]=20
# print(numbers) #'tuple' object does not support item assignment

# shopping=['laptops','keyboard','headset']
# shopping.append('Smartphone')
# print(shopping)

# days=(
#     "Monday",
#     'Tuesday',
#     'wednesday',
#     'Thursday',
#     'Friday',
#     'Satday'
#     'sunday'
# )



# def decorator(func):
#     def wrapper():
#         print("Before Function")
#         func()
#         print("After fuctions")
#     return wrapper

# @decorator
# def greet():
#     print("hello Welcome")

# greet()


# import time
# def timer(func):
#     def wrapper():
#         start=time.time()
#         func()
#         end=time.time()
#         print("Time:",end-start)
#     return wrapper

# @timer
# def task():
#     print("Working")

# task()



#Reverser a String

# text="python"
# string=""

# for char in text:
#     string=char + string

# print(string)

# text_1="Python is a easy  language "
# print(text_1[::-1])

text_2="Reverse a string"
print("".join(reversed(text_2)))