#import pandas as pd
#-*- encoding: utf-8 -*-

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

with open(r'C:\Users\ASUS\Desktop\Assssss.txt', 'r',encoding='UTF16') as file:
    data = file.read().replace('\n', ' ')
    data2=data.replace('\t', ' ')

docAS=data2.split(' ')
print(len(docAS))
#print(docA)

#stop Word removal attempt(see prototype.py)
fh=open(r'C:\Users\ASUS\Desktop\stop_words_as.txt','r',encoding='UTF-16-le')
fh2=fh.read()


for word in data2:
    for w in fh2:
        if(word==w):
           data2=data2.replace(w,'')
docA=data2.split(' ')
print(len(docA))
docB = "কিন্তু প্ৰকৃততে যি পৰিবেশ আৰু পটভূমি অসমীয়া উপন্যাস সাহিত্যত প্ৰতিষ্ঠা হয়"
bowA = docA
bowB = docB.split(" ")
#print(bowA)
#print(bowB)
wordSet = set(bowA).union(set(bowB))
#print(wordSet)
wordDictA = dict.fromkeys(wordSet, 0) 
wordDictB = dict.fromkeys(wordSet, 0)
#print(wordDictA)
for word in bowA:
    wordDictA[word]+=1
    
for word in bowB:
    wordDictB[word]+=1

#print(wordDictA)
#print(wordDictB)

#pd.DataFrame([wordDictA, wordDictB])


tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)

#print(tfBowA)

idfs = computeIDF([wordDictA, wordDictB])
#print(idfs)

tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)

print(tfidfBowA)
#print(tfidfBowB)
#print(pd.DataFrame([tfidfBowA, tfidfBowB]))
