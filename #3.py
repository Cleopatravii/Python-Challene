import re
filein = open("challenge4.html","r")
for k in range(21):
    filein.readline()
text = filein.read()
letters= list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
lettlist=[]
firstlist=[]
for i in text:
    for j in letters:
        if i==j:
            lettlist.append(i)
#print len(lettlist)lettlist
firstlist = re.findall(r"[^A-Z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][^A-Z]", text)
print firstlist
firstlist1= re.findall(r"[A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z]","".join(firstlist))
text1 = "".join(firstlist1)
print text1
print "".join(re.split(r"[A-Z][A-Z][A-Z]", text1))

#print (re.findall('[A-Z]{3}[a-z][A-Z]{3}', "BAAAaAAA"))
