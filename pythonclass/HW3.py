import random

working_days = ["Sunday","Monday","Tuesday","Thursday","Friday",]
name_of_students = ["Pratyush","Sallu Bhai","Elon Musk","Narendra Modi","Bill Gates","K.P Oli"]
random.shuffle(working_days)
random.shuffle(name_of_students)
for students,day in zip (name_of_students,working_days):

 print(f"{students} is assigned to : {day}")

# import random
# def print_presentations():
#  presentors =["Pratyush","Sallu Bhai","Elon Musk","Modi","Bill Gates","K.P Oli"]
#  random.shuffle(presentors)
#  for day,presentor in enumerate(presentors,start=1):
#      print(f"{presentor} has presentation on day{day}")
# print_presentations()

