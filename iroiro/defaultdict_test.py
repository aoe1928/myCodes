from collections import defaultdict

d = ['aab', 'abdj', 'ccde', 'ehi']

dd = defaultdict(lambda: 1)
print(dd)

for i in d:
    dd[i[0]] += 1
print(dd)