from src import AOC2022 as ao

f = ao.read_file('./data/day4_test.txt')
matches = 0
matches2 = 0
for row in f:
    row = row.split(',')
    # print(row)
    n1, n2 = tuple(row[0].split('-'))
    n3, n4 = tuple(row[1].split('-'))
    r1 = range(int(n1), int(n2)+1)
    r2 = range(int(n3), int(n4)+1)

    r3 = [x for x in r1 if x not in r2]
    r4 = [x for x in r2 if x not in r1]

    r5 = [x for x in r1 if x in r2]
    r6 = [x for x in r2 if x in r1]

    if len(r3) == 0 or len(r4)==0:
        print(row)
        matches = matches + 1
    if len(r5) > 0 or len(r6) >0:
        matches2 = matches2 +1
    
print(f'fully contained pairs: {matches}')
print(f'overlapping pairs: {matches2}')
#       r4 = [x for x in r2 if x not in r1]


#     r1 = range(int(row[0].split('-')[0]), int(row[0].split('-')[1]))
#     r2 = range(int(row[1].split('-')[0]), int(row[1].split('-')[1]))
#     r3 = [x for x in r1 if x not in r2]
#     r4 = [x for x in r2 if x not in r1]
#     # print(r3, r4)
#     if (len(r3) == 0 or len(r4) == 0):

#         matches = matches +1
#         print(row)
# print(matches)