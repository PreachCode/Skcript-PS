str=list(input())									# inputting the string as an array
n=len(str)										# storing the length in n
sum=0;
for ch in str:
	if ch=='1':
		sum=sum+1								# sum calculates the number of 1s
if sum%2==0:
	print("no solution")
else:
	pos=-1
	for i in range(0,n):								# this is algorithm part where go till the first 1
		if str[i]=='1':								# remove it recursively backwards
			for j in range(i,pos,-1):
				print(j, end=' ')
			pos=i
			if i!=n-1:
				if str[i+1]=='0':
					str[i+1]='1'
				else:
					str[i+1]='0'
