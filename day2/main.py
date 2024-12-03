
with open('input.txt') as f:
    lines = f.readlines()

list_tuples = [l.strip().split(' ') for l in lines]
reports = [[int(e) for e in t] for t in list_tuples]

print(reports)