from src import AOC2022 as ao

f  = ao.read_file('./data/day1_test.txt')
f=[x for x in ((" ".join(f)).split("  "))]
f=[x.split(' ') for x in f]
# print(f)
elf_cals = {}
for i, e in enumerate(f):
    # print(i)
    elf_cals[i+1] = sum(int(x) for x in e)
max_elf = max(elf_cals, key = elf_cals.get)
print(f'Elf number {max_elf} has the most calories: {elf_cals[max_elf]}')
max_3_elves_vals = list(dict(sorted(elf_cals.items(), key=lambda item: item[1], reverse=True)).values())[:3]
max_3_elves_keys = list(dict(sorted(elf_cals.items(), key=lambda item: item[1], reverse=True)).keys())[:3]
print(f'Elves number {max_3_elves_keys} have the most total calories: {sum(max_3_elves_vals)}')

