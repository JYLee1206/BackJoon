A, B, C = map(int,input().split())

award = 0
MAX = [A, B, C]

MAX = max(MAX)

#주사위 비교
if A==B==C:
    award = 10000+(A*1000)
elif A==B or A==C:
    award = 1000+(A*100)
elif B==C:
    award = 1000+(B*100)
else :
    award = MAX*100

print(award)