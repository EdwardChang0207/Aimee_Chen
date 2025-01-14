x = int(input())

#for loop:
l = []
for i in range(2,x+1):
    if x%i == 0:
        l.append(i)
print(l)

#while loop:
l = []
index = 2
while index <= x:
    if x % index == 0:
        l.append(index)
    index += 1
print(l)