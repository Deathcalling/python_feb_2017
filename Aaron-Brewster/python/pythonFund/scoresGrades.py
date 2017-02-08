def scoreGrade():

    import random
    x = ''
    score = 0

    for i in range(1, 10):
        score = random.randint(60, 100)
        if(score >= 90):
            x = 'A'
        elif(score >= 80):
            x = 'B'
        elif(score >= 70):
            x = 'C'
        elif(score >= 60):
            x = 'D'
        print('Score:', score, ' Your grade is', x)

scoreGrade()
