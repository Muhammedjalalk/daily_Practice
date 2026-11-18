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
my_array=array.array([10,20,30])
print(my_array)