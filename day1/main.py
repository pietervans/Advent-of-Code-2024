
with open('input.txt') as f:
    lines = f.readlines()

tuple_list = [l.strip().split(' ') for l in lines]
l1 = sorted([int(t[0]) for t in tuple_list])
l2 = sorted([int(t[-1]) for t in tuple_list])

res = 0
for n1 in l1:
    c = l2.count(n1)
    res += n1*c

print(res)
