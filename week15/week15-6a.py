a,b,c,d=list(map(int,input().split()))

ans=(a-c)*(b-d)
ans=abs(ans)
print(ans,end='')