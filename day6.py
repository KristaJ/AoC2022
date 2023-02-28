from src import AOC2022 as ao

f = ao.read_file('./data/day6_test.txt')
for l in f:
    for i in range(len(l)):
        if len(list(set(l[i:i+4]))) == 4:
            print(f'first set of 4 unique chars from  {i} to {i+4}')
            break
for l in f:
    for i in range(len(l)):
        if len(list(set(l[i:i+14]))) == 14:
            print(f'first set of 14 unique chars from  {i} to {i+14}')
            break
