from src import AOC2022 as ao

def score_items(l):
    score = 0
    for d in l:
        if d.isupper():
            score = score + ord(d)-38
        else:
            score = score + ord(d)-96
    return score

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

f = ao.read_file('./data/day3_test.txt')
packs = [(x[:int(len(x)/2)], x[int(len(x)/2):]) for x in f]
duplicates = []
for p in packs:
    counter = {}
    unique = list(set(p[0])) + list(set(p[1]))
    for letter in unique:
        counter[letter] = counter.get(letter, 0) + 1
    duplicates.extend([k for k,v in counter.items() if v>1])
score = score_items(duplicates)
print(score)

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

groups = list(divide_chunks(f, 3))
badges=[]
for g in groups:
    counter={}
    group_pack = [list(set(x)) for x in g]
    all_items = [item for sublist in group_pack for item in sublist]
    for item in all_items:
        counter[item] = counter.get(item, 0) + 1
    badges.extend([k for k,v in counter.items() if v==3])
print(score_items(badges))
