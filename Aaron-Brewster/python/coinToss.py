def coinToss():

    import random
    x = ''
    attempts = 0
    countHeads = 0
    countTails = 0
    toss = 0

    for i in range(1, 5001):
        toss = random.randint(1, 100)
        attempts += 1
        if(toss >= 50):
            countHeads += 1
            x = 'It\'s a head!'
        elif(toss < 50):
            countTails += 1
            x = 'It\'s a tail!'
        print('Attempt {}: Tossing coin... {} ... Got {} head(s) so far and {} tail(s) so far.'.format(attempts, x, countHeads, countTails))

coinToss()
