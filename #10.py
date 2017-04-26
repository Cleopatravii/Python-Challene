import re
Curr='1'
for i in range(30):    
    match=re.findall('(\d)(\\1*)', Curr)
    Curr= ''.join([str(len(x+y))+x for x,y in match])
print len(Curr)
