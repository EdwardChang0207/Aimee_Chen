l = [1,2,3]
for i in l:
    i += 1 #-> (新的)i = (原本的)i + 1
print(l)
for i in range(len(l)):
    l[i] += 1
print(l)
