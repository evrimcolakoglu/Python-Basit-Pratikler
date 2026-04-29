import random

HaftalikSicaklik = []

for x in range(7):
    x = random.randint(1,35)
    HaftalikSicaklik.append(x)

print(HaftalikSicaklik)
print(int(sum(HaftalikSicaklik)/len(HaftalikSicaklik)))
    
