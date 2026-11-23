x="hello"
print(x[1:4],x[-1:])


#Example of append and Extend 
x=[1]
# x.append([2,3])
x.extend([2,3])
print(x)



#dictinary unique key check
print(len({1:'a',1:"b"}))

#Practical Question
d={'name':"Jalal"}
print(d.get('age',25))


#different between list and Array
import array
my_array=array.array('i',[10,20,30])
print(my_array)


#Predict output
x=[1,2,3]
y=x
y.append(4)
print(x)


#What is a base case in recursion
def count(n):
    if n==0:
        return 

    print(n)
    count(n-1)
count(6)