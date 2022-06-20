STU = 5

scores = []
scoreSum = 0
scoreAvg = 0

def SCR():
    global scoreSum
    for i in range(STU):
        value = int(input("성적 입력"))
        scores.append(value)
        scoreSum += value

def AVG():
    global scoreAvg
    scoreAvg = scoreSum / len(scores)
    
def NOS():
    global highScoreStudents
    highScoreStudents = 0
    for i in range(len(scores)):
        if scores[i] >= 80:
            highScoreStudents += 1
            
SCR()
AVG()
NOS()


        
print("성적 평균은", scoreAvg,"입니다")
print("80점 이상 성적을 받은 학생은", highScoreStudents,"입니다")

