l = [3,6,6,7,8,1,5,6,5,3,5]

size = len(l)
key = int(input("Enter the element to be removed"))

i = 0 

while i < size:
	for j in range(size):
		if j == size:
			break
		if l[j] == key:
			pos = j 
			for m in range(pos,size-1):
				l[m] = l[m+1]
			size-=1
			l.pop()
	i+=1
print(l)

c = 0 


for m in range(size - 1,-1,-1):
	for j in range(m):
		if l[m] == l[j]:
			l.remove(l[j])
			break
print(l)

