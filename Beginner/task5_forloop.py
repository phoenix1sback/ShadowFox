import random
count_6=0
count_1=0
two_6=0
previous=0
for i in range(20):
    roll=random.randint(1,6)
    print(roll)
    if roll==6:
        count_6 +=1
    if roll==1:
        count_1 +=1
    if previous ==6 and roll==6:
        two_6 +=1
previous=roll
print("number of 6s",count_6)
print("number of 1s ",count_1)
print("number of 2 sixes is ",two_6)
#2
total=100
completed =0
for i in range(10):
    completed += 10
    print("u complted",completed,"jumping racks")
    if completed ==100:
        print("u complted 100 racks and u r amazing")
        break
    tired=input("r u tired?")
    if tired=="yes" or tired=="y":
       skip=input("do u want to skip the racks ")
       if skip =="yes" or skip=="y":
           print("u have completed",completed,"number of racks")
    break
print("remaining racks",total-completed)
  