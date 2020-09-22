f = open('continents.txt','r')
s = f.read()
s = s.replace('\n',' ')
l = s.split()
print(len(l))

