#@ Static method doesn't Receive self or class 
#it behaves like a normal functions,but it kept inside the class  becouse it is  related to the class 

class Calulator:
    @staticmethod
    def add(a,b):
        return a +b
print(Calulator.add(20,30))


#Example class Fuctions 
class Student:
    school="ABC school"

    @classmethod

    def show_school(cls):
        return cls.school
print(Student.show_school())


#GIL-Standard for Global interpter lock

# Example
import threading
import time
def dowload():
    time.sleep(2)
    print("Dowloaded Completed")

t1=threading.Thread(target=dowload)
t2=threading.Thread(target=dowload)

t1.start()
t2.start()

t1.join()
t2.join()
