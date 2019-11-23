
import nltk
import pandas as pd
#-*- encoding: utf-8 -*-

#computation of TF

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

#computation of IDF

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

#computation of TF-IDF

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

#preprocessing: Stop words Removal

def stop_remove(f):
    with f as file:
        data = file.read().replace('\n', ' ')
        data2=data.replace('\t', ' ')

    docAS=data2.split(' ')

    fh=open(r'C:\Users\ASUS\Desktop\stop_words_ass.txt','r',encoding='UTF16')   #stop words file
    fh2=fh.read()

    wt=nltk.word_tokenize(fh2)

    for word in docAS:
        if word in wt:
            docAS.remove(word)
            return docAS
    
f=open(r'C:\Users\ASUS\Desktop\as.txt', 'r',encoding='UTF16')       #file to calculate TF_IDF
docA= stop_remove(f)
print(docA)
docB = "কিন্তু প্ৰকৃততে যি পৰিবেশ আৰু পটভূমি অসমীয়া উপন্যাস সাহিত্যত প্ৰতিষ্ঠা হয়"  #test sentence, can add another file here also
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
