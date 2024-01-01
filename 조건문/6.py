H, M = map(int,input().split()) 
t = int(input())

H = ((H*60) + (M+t))//60
M = (M + t)%60
if H>=24:
    H -=24

print(H, M)