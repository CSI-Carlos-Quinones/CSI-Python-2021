from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

name = input("Hello there! What is your name? ")
studentId = input("What is your student id? ")

if name == "Carlos Quiñones":
  print("Hello me!!")
else:
  print(f" Your name is: {name} ")


print(f"Your Student id is: {studentId} ")
print(f"Currently, the time is: {current_time} ")
