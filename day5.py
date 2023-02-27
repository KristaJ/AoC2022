from src import AOC2022 as ao
import re

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

f = ao.read_file2('./data/day5_test.txt')
stacks = []
instructions = []
intruction_part=False
for l in f:
    if l == '':
        intruction_part=True
    elif not intruction_part:
        stacks.append(l)
    else:
        instructions.append(l)
order = [int(x) for x in stacks[-1].split('  ')]
stacks = [re.findall('(.{3})\W?', x) for x in stacks[:-1]]
stack_dict={}
for i in order:
    stack_dict[i]=[x[i-1] for x in stacks[::-1] if len(x)>=i and len(x[i-1].strip())>0]

# print(instructions)
# print(stack_dict)

for i in instructions:
    num_move, from_stack, to_stack = re.match('move (\d+) from (\d+) to (\d+)', i).groups()
    # print(num_move, from_stack, to_stack)
    for n in range(int(num_move)):
        stack_dict[int(to_stack)].append(stack_dict[int(from_stack)].pop())
print(''.join([x[-1][1] for x in stack_dict.values()]))






stacks = []
instructions = []
intruction_part=False
for l in f:
    if l == '':
        intruction_part=True
    elif not intruction_part:
        stacks.append(l)
    else:
        instructions.append(l)
order = [int(x) for x in stacks[-1].split('  ')]
stacks = [re.findall('(.{3})\W?', x) for x in stacks[:-1]]
stack_dict={}
for i in order:
    stack_dict[i]=[x[i-1] for x in stacks[::-1] if len(x)>=i and len(x[i-1].strip())>0]

# print(instructions)
# print(stack_dict)
for i in instructions:
    num_move, from_stack, to_stack = re.match('move (\d+) from (\d+) to (\d+)', i).groups()
    # print(num_move, from_stack, to_stack)
    n=int(num_move) * -1
    stack_dict[int(to_stack)].extend(stack_dict[int(from_stack)][n:])
    stack_dict[int(from_stack)] = stack_dict[int(from_stack)][:n]
print(''.join([x[-1][1] for x in stack_dict.values()]))

