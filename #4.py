import urllib, re
url ="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothinglist=[]
nothing = "12345"
for i in range(400):
    string = urllib.urlopen(url + nothing)
    string1 = string.read()
    string2 = string1.decode("utf8")
    string.close()
    nothing0 = str(re.findall(r"[0-9]",string2))
    
    nothing= "".join(re.findall(r"[0-9]",nothing0))
    nothinglist.append(nothing)
print nothinglist
