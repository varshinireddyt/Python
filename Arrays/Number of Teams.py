
from math import comb
def numberOfTeams(num,skills,minAssociates,minLevel,maxLevel):
    count = 0
    for i in range(len(skills)):
        if minLevel <= skills[i] <= maxLevel:
            count += 1
    sum = 0
    while minAssociates <= count:
        sum = sum + comb(count,minAssociates)
        minAssociates += 1
    return sum
num = 6
skills = [12, 4, 6, 13, 5, 10]
minAssociates = 3
minLevel = 4
maxLevel = 10

print(numberOfTeams(num,skills,minAssociates,minLevel,maxLevel))


