str=list(input())
n=len(str)
sum=0;
for ch in str:
	if ch=='1':
		sum=sum+1
if sum%2==0:
	print("no solution")
else:
	pos=-1
	for i in range(0,n):
		if str[i]=='1':
			for j in range(i,pos,-1):
				print(j, end=' ')
			pos=i
			if i!=n-1:
				if str[i+1]=='0':
					str[i+1]='1'
				else:
					str[i+1]='0'
