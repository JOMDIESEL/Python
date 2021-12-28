def grade_of_student():
    print("Please input your name!!")
    name  = str(input())
    print("Please input your score !!")
    score = float(input())
    if score >= 80 and score <=100  :
        print("Name is {} score = {} Grade = A".format(name,score))
    elif score >=70 and score<80:
        print("Name is {} score = {} Grade = B".format(name,score))
    elif score >=60 and score<70 :
        print("Name is {} score = {} Grade = C".format(name,score))
    elif score >=50 and score<60  :
        print("Name is {} score = {} Grade = D".format(name,score))
    elif score >=0 and score <50  :
        print("Name is {} score = {} Grade = F".format(name,score))
    else :
        print("Name is {} score = {} is wrong.".format(name,score))
while True:
    grade_of_student()   