import os
data={}
datal={}
c=1
temp=[]
dataw=[]
m=set()
with open("sample.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        #print(line)
        temp=line
        data[c]=temp.split()
        data[c].sort()
        print("data",data[c])
        c=c+1
for num in range(1,len(data)+1):
    for word in range(1,len(data.[num]))
    dataw.append(data[num])
    print(dataw)
c=1
with open("trainsample.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        datal[c]=line
        print("lab",datal[c])
        c=c+1
        
