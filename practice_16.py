employee_details={
101:{"name":"Arun","department":"Computer Science","Salary":20000},
102:{"name":"Rahul","department":"Python","Salary":25000},
103:{"name":"Anu","department":"Java","Salary":30000},
104:{"name":"Vishnu","department":"python","Salary":220000},
105:{"name":"Meera","department":"Computer Science","Salary":280000},

}

for data in employee_details.values():
    # max_salary=0
    found=False
    
    # if data["department"]=="Computer Science":
    #     print(data["name"])
    # if data["Salary"]>max_salary:
    #     max_salary=data["Salary"]
    if data["Salary"]<3000:
            # max_salary=data["Salary"]

        print(data["department"],data["Salary"])
        found=True
if not found:
        
        print("no employee Exit")

# print(max_salary)

    
        
# students=[
#         {"id":1,"name":"Jalal","age":22,"department":"cs", "mark":85},
#           {"id":2,"name":"Rahul","age":21,"department":"Bca", "mark":90},
#             {"id":3,"name":"Arun","age":23,"department":"cs", "mark":75},

# ]
# for data in students:
#      if data["mark"]>80:
#           print(data['name'],data["mark"])



print(hash(10))
print(hash("jalal"))
print(hash((1,2,3,4)))

student={
     "jalal","Rahul","Arun"
}
print('jalal' in student)


a=10
print(type(a))
print(isinstance(a,float))