from src import AOC2022 as ao

f  = ao.read_file('./data/day2_test.txt')
# A,X = rock
# B,Y = paper
# C,Z = scisors

win = {'A':'Y', 'B':'Z', 'C':'X'}
draw = {'A':'X', 'B':'Y', 'C':'Z'}
loss = {'A':'Z', 'B':'X', 'C':'Y'}
me_points  = {'X':1, 'Y':2, 'Z':3}
outcome = {'X':'lose', 'Y':'draw', 'Z':'win'}
op2me  = {'A':'X', 'B':'Y', 'C':'Z'}
score = 0
for round in f:
    op = round[0]
    me = round[2]
    score = score + me_points[me]
    if win[op] == me:
        score = score +6
    elif op2me[op] == me:
        score = score + 3
print(f'score round 1 = {score}')

score2=0
for round in f:
    op = round[0]
    oc = outcome[round[2]]
    
    if oc == 'win':
        me = win[op]
        score2 =  score2+6+me_points[me]
    elif oc == 'lose':
        me = loss[op]
        score2 =  score2+me_points[me]
    else:
        me = draw[op]
        score2 =  score2+3+me_points[me]
print(f'score round 2 = {score2}')


