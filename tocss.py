import os
data=[]
datal=[]
datat=[]
c=1
temp=[]
vocabulary=[]
count0=[]
count1=[]
countall=[]
countdata=[]
c=0
p0=1
p1=1
c0=0
c1=0
ct0=0
ct1=0
label=5
accuracy=0
stop=[]
with open("traindata.txt","r") as f: #vocabulary
    lines=f.readlines()
    for line in lines:
        temp=line
        data=temp.split()
        for word in data:
            vocabulary.append(word)
        vocabulary=list(set(vocabulary))
        vocabulary.sort()
        #print("data",vocabulary)
        
with open("trainlabels.txt","r") as f: #count how many 0 and 1 in training
    lines=f.readlines()
    for line in lines:
        a=int(line.strip())
        datal.append(a)
        if(a==0):
            c0=c0+1
        if(a==1):
            c1=c1+1
#print("p0",p0)
#print("p1",p1)
#print("lab",len(datal))

with open("stoplist.txt","r") as f: #stoplist
    lines=f.readlines()
    for line in lines:
        temp=line.strip()
        #print(temp)
        stop.append(temp)        
        if temp in vocabulary:
            vocabulary.remove(temp)

print(vocabulary)


#print(stop)
for num in vocabulary:
    count0.append(0)
    count1.append(0)
    countdata.append(0)
g=0

with open("traindata.txt","r") as f: #count word times 
    lines=f.readlines()
    for line in lines:
        temp=line.strip().split()   
        
        
        temp=list(set(temp))
        temp.sort()
        #print(temp)
        for num in (stop):
            if num in temp:
                temp.remove(num)
        #print(temp)    
        for word in temp:
            
                if word in vocabulary:                 
                    if datal[c]==0:
                        if(c==10000):                            
                            print("in0",count0[vocabulary.index(word)])
                            
                        count0[vocabulary.index(word)]=count0[vocabulary.index(word)]+1
                                                
                    if datal[c]==1:
                        if(c==10000):
                            print(word)
                            print("in1",vocabulary.index(word))
                        count1[vocabulary.index(word)]=count1[vocabulary.index(word)]+1                 
                
        c=c+1              
#print(count0)
#print(count1)
c=0
with open("traindata.txt","r") as f: #accuracy of training 
    lines=f.readlines()
    fp=open("output_train.txt","a")
    for num in range (len(countdata)):
        strn=str(num)
        fp.write(strn)
        fp.write(",")
    fp.write("class\n")
    fp.close()
    for line in lines:
        temp=line.strip().split()
        
        temp=list(set(temp))
        temp.sort()       
        for num in (stop):
            if num in temp:
                temp.remove(num)
        
        for word in temp:
            for num in range(len(vocabulary)):
                if word in vocabulary[num]:            
                    countdata[num]=1
                    #print(word)
                    #print("in1",vocabulary.index(word))
        for num in range(len(countdata)):           #Laplace Smoothing
            if countdata[num]==0:
                p1=p1*((c1-count1[num]+1)/(c1+2))  
                p0=p0*((c0-count0[num]+1)/(c0+2))
            if countdata[num]==1:
                p1=p1*((count1[num]+1)/(c1+2))
                p0=p0*((count0[num]+1)/(c0+2))
        fp=open("output_train.txt","a")
        for num in range(len(countdata)):
            strt=str(countdata[num])
            fp.write(strt)
            fp.write(",")
        strd=str(datal[c])
        fp.write(strd)
        fp.write("\n")
        fp.close()
        
        #print(countdata)
        p1=p1*(c1/(c1+c0))        
        p0=p0*(c0/(c1+c0))

        if p1>p0:
            label=1            
        if p1<p0:
            label=0
        if datal[c]==label:
            accuracy=accuracy+1
            #print(accuracy)
        for num in range(len(countdata)):     
            countdata[num]=0
        p1=1
        p0=1
        c=c+1
print("accuracy",accuracy/len(datal))


with open("testlabels.txt","r") as f: #count how many 0 and 1 in test
    lines=f.readlines()
    for line in lines:
        a=int(line.strip())
        datat.append(a)
        if(a==0):
            ct0=ct0+1
        if(a==1):
            ct1=ct1+1
c=0
accuracy=0
with open("testdata.txt","r") as f: #accuracy of testing 
    lines=f.readlines()
    fp=open("output_test.txt","a")
    for num in range (len(countdata)):
        strn=str(num)
        fp.write(strn)
        fp.write(",")
    fp.write("class\n")
    fp.close()    
    for line in lines:
        temp=line.strip().split()
        temp=list(set(temp))
        temp.sort()
        for num in (stop):
            if num in temp:
                temp.remove(num)
        for word in temp:
            for num in range(len(vocabulary)):
                if word in vocabulary[num]:            
                    countdata[num]=1
        for num in range(len(countdata)):          #Laplace Smoothing
            if countdata[num]==0:
                p1=p1*((c1-count1[num]+1)/(c1+2))
                p0=p0*((c0-count0[num]+1)/(c0+2))
            if countdata[num]==1:
                p1=p1*((count1[num]+1)/(c1+2))
                p0=p0*((count0[num]+1)/(c0+2))
        fp=open("output_test.txt","a")
        for num in range(len(countdata)):
            strt=str(countdata[num])
            fp.write(strt)
            fp.write(",")
        strd=str(datat[c])
        fp.write(strd)
        fp.write("\n")
        fp.close()
        p1=p1*(c1/(c1+c0))
        p0=p0*(c0/(c1+c0))
  
        if p1>p0:
            label=1            
        if p1<p0:
            label=0
        if datat[c]==label:
            accuracy=accuracy+1
            #print(accuracy)
        for num in range(len(countdata)):     
            countdata[num]=0
        p1=1
        p0=1
        c=c+1
#print(len(datat))

print("accuracy",accuracy/len(datat))
        
