
#== Value Compersion 
#Check whether to objects have same value

a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)

# is Done identity Compersion
#Check Whether both Varibles are Refer to the same object
a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(a is b)

#interview Questions
a=[10,20]
b=a
print(a==b) #Both Varible is Refered to same Objects

print(a is b)


# == → Are the values equal?
# is → Are they the same object?


#list Comprehension Vs Generator Expression

#List Comprehension Create  the entire list immediately and store all value in Memory
squares=[x * x for x in range(10)]
print(squares)
#it possible to Acces elment Directly
print(squares[4])

#Generator Expression 
#A Generator expression doesn't create all values immediately.it generator each value only needed
squares=(x *x for x in range(8))
print(next(squares))
print(next(squares))


#Decorator is a function that modifies or extand the behavior of another 
# function without change this riginal code
import time
from  functools import wraps
def execution_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.perf_counter()
        result=func(*args,**kwargs)
        end=time.perf_counter()
        print(f"{func.__name__} took {end-start:.4f} seconds") 
        return result
    return wrapper

@execution_time
def test():
    time.sleep(2)
    return "Done"

print(test())