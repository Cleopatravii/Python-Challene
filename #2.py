filein = open("challenge3.html", "r")
for k in range(37):
    filein.readline()
lines = list(filein.read())
list1= list("abcdefghijklmnopqrstuvwxyz")
out=[]
for i in lines:
    for j in list1:
        if i==j:
            out.append(j)
            
print "".join(out)
