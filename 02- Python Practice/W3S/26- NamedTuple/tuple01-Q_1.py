from collections import namedtuple

Student = namedtuple("student", ["name", "age", "marks"])


student1 = Student("Maitreya", 22, {"Math": 85, "Science": 90, "History": 78, "English": 92, "Art": 88})
student2 = Student("Markie", 22, {"Math": 75, "Science": 82, "History": 95, "English": 88, "Art": 90})
student3 = Student("Aduuuu", 21, {"Math": 92, "Science": 87, "History": 85, "English": 78, "Art": 91})


print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Marks:", student1.marks)

print("\nStudent 2:")
print("Name:", student2.name)
print("Age:", student2.age)
print("Marks:", student2.marks)

print("\nStudent 3:")
print("Name:", student3.name)
print("Age:", student3.age)
print("Marks:", student3.marks)
