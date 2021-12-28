result = dict({})
def grade_of_student(name,score):  
    if score >= 80 and score <=100 :
        score_a = ("Score = {} Grade = A".format(score))
        result.update({name:score_a})
    elif score >=70 and score<80:
        score_b = ("Score = {} Grade = B".format(score))
        result.update({name:score_b})
    elif score >=60 and score<70 :
        score_c = ("Score = {} Grade = C".format(score))
        result.update({name:score_c})
    elif score >=50 and score<60  :
        score_d = ("Score = {} Grade = D".format(score))
        result.update({name:score_d})
    elif score >=0 and score <50  :
        score_f = ("Score = {} Grade = F".format(score))
        result.update({name:score_f})
    else :
        score_g = ("Score = {} is wrong.".format(score))
        result.update({name:score_g})
    
for x in range(10):
    print("Please input your name !!")
    name  = str(input())
    print("Please input your score !!")
    score = float(input())
    grade_of_student(name,score)
    print(result)
for key, value in result.items():
    print("Name : "+key+" "+value)
     



        
