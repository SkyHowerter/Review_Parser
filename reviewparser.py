#Logan Howerter
#assignment 3
#March 7th
import math 
listwords=["<s>"]
yn = raw_input("do you have your own gold-standard files in the current directory? y/n:")
if(yn=="y"):
    filename1 = raw_input("What's the name of your positive, gold-standard file?")
    filename2 = raw_input("What's the name of your negative, gold-standard file?")
else:
    filename1='hotelPosT-train.txt'
    filename2='hotelNegT-train.txt'
print("I'm processing the files I was loaded with.")

with open(filename1,'r') as f: #this opens the corpus, and begins making a list of every word in the corpus, with one entry per word
    for line in f:
        flag=0
        for word in line.split():
            i=0
            if(flag==0):
                i=len(listwords)+1
                flag=1
            while(i<len(listwords)):
                if(listwords[i]==word):
                    i=len(listwords)+1
                i=i+1
            if(i<len(listwords)+1):
                listwords.append(word)
with open(filename2, 'r') as f:
    for line in f:
        flag=0
        for word in line.split():
            i=0
            if(flag==0):
                i=len(listwords)+1
                flag=1
            while(i<len(listwords)):
                if(listwords[i]==word):
                    i=len(listwords)+1
                i=i+1
            if(i<len(listwords)+1):
                listwords.append(word)   

uniposcounts=[1 for i in range(len(listwords))] #initialize unicount arrays with plus one smoothing
uninegcounts=[1 for i in range(len(listwords))]
with open(filename1,'r') as f: #fill out positive unicount array
    for line in f:
        for word in line.split():
            i=0
            while(i<len(listwords)):
                if(listwords[i]==word):
                    uniposcounts[i]+=1
                    i=len(listwords)
                i+=1
with open(filename2,'r') as f: #fill out negative unicount array
    for line in f:
        for word in line.split():
            i=0
            while(i<len(listwords)):
                if(listwords[i]==word):
                    uninegcounts[i]+=1
                    i=len(listwords)
                i+=1

def unigramprob(sent):#this function calculates the probablility of a sentance being positive or negative based on the unigram model and outputs that probability
    global listwords
    global unicounts
    prob=.5
    flag=0
    for word in sent.split():
        i=0
        if(flag==0):
            tbr=word
            flag=1
        while(i<len(listwords)):
            if(listwords[i]==word):
                prob=prob-math.log(uniposcounts[i], 10)+math.log(uninegcounts[i],10) #this line pushes "prob" negative for a positive review, and postivie for a negative review. 
                i=len(listwords)
            i+=1
    return tbr, prob
collectorp = 0.0
collectorn = 0.0
yn = raw_input("Do you have your own test set to use in this directory? y/n:")
if(yn=="y"):
    ts = raw_input("What's the name of your test file?")
else:
    ts="test-set.txt"
with open(ts,'r') as f: #this outputs all of the test sentence POS or NEG flags to the necessary file
    with open('your-test-set-answers.txt', 'w+') as g:
        for line in f:
            tid, temp=unigramprob(line)
            if(temp<0):
                g.write(tid + " POS" +"\n")
                collectorp = collectorp + 1
            if(temp>=0):
                g.write(tid + " NEG" +"\n")
                collectorn = collectorn + 1
print("Your test set had " + str(collectorp) + " positive reviews, and " + str(collectorn) + " negative reviews.")
print(str(collectorp/(collectorp+collectorn)) + "% of the reviews were positive.")
