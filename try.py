# x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in x:
#     if i % 2 == 0:
#         print(i,end=" ")

# square = [1,2,3,4,5]
# newList = []
# for i in square:
#     newList.append(i**2)

# print(newList)

# aList = ["apple","banana","orange","strawberry","Guava","Tengrent",'milk']
# print(aList[2:7])

# squares = [x**2 for x in range(1,11)]
# print(squares)

# newItems = [1,2,3,3,4,5,5]
# itens = []
# for item in newItems:
#     if item not in itens:
#         itens.append(item)
# print(itens)    

# x = {x*x for x in range(1,6)}
# print(x)

# def merge_dictionaries(dict1, dict2):
#   """Merges two dictionaries into one, handling duplicates.

#   Args:
#     dict1: The first dictionary.
#     dict2: The second dictionary.

#   Returns:
#     A new dictionary with the merged contents of dict1 and dict2.
#   """

#   merged_dict = dict1.copy()
#   for key, value in dict2.items():
#     if key in merged_dict:
#       # If the key already exists, update the value
#       merged_dict[key] = [merged_dict[key], value]
#     else:
#       # If the key is new, add it to the dictionary
#       merged_dict[key] = value
#   return merged_dict

# # Example usage
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# merged_dict = merge_dictionaries(dict1, dict2)
# print(merged_dict)  # Output: {'a': 1, 'b': [2, 3], 'c': 4}


# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
#     def update_grade(self,new_grade):
#         self.grade = new_grade
#     def display_info(self):
#         print(f"this student name is {self.name} and has a grade {self.grade}")

# st1  = Student("seif", "B")
# st1.display_info()        


# try:

#   class Student:

#     all_student = []
#     def __init__(self, name, grade):
#       self.name = name
#       self.grade = grade
#     def update_grade(self, new_grade):
#       self.grade = new_grade
      

#     def display_info(self):
#       print(f"This student's name is {self.name} and has a grade {self.grade}")

#   st1 = Student("seif", "B")
#   st1.display_info()
#   st1.update_grade("A+")
#   st1.display_info()
# except:
#   print("Error")


# class Car:
#     def __init__(self, speed=0):
#             self.speed = speed
#     def increment(self, new_speed):
#             self.speed += new_speed
#     def decrement(self, decrese):
#         self.speed -= decrese
#         if decrese <= 0:
#             self.speed = 0
#     def declare(self):
#             print(f"current speed of the car is {self.speed}")
# try:            
#     car = Car()
#     car.increment(50)
#     car.decrement(20)
#     car.declare()                
# except Exception as e:
#     print("Why")


class School:
    def __init__(self,nameOfSchool):
        self.nameOfSchool = nameOfSchool
class Student(School):
    def __init__(self,id,SchoolName):
        self.id = id
        self.SchoolName = SchoolName
    def transfer_school(self):
        if self.nameOfSchool != self.SchoolName:
            self.SchoolName = self.nameOfSchool
        else:
            self.nameOfSchool = self.SchoolName
    def declare(self):
        print(f"the student in {self.nameOfSchool} school")
st1 = Student(34,"We school")
st1.declare()                