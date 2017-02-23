import re
import os
import sys
import math
from collections import OrderedDict

all_words = {} # frequencies of all words
docs = 0

doc_words = {} # words in docs by filename
doc_numwords = {} # number of words in doc by filename

doc_tf = {} # tf by filename
corpa_idf = {} # idf by word
doc_tfidf = {} # tfidf by filename

def shorten_word(word):
    sword = re.match("^.+((?=(e|er|erne|est|en|et|ene)))", word)
    if sword == None:
        sword = word
    else:
        sword = sword.group(0)
    return sword

def frequency(file):
    fo = open(file)
    text = fo.read()
    words_dict = {}
    
    fo.close()
    
    #print(re.split("\s*\.*\,*\n*|(<[\\]?[a-z])", text))
    text_list = re.split("[\s\.\,\"\:\;\'\(\)\?\!]+", text)
    
    for word in text_list:
        lword = word.lower()

        if lword in words_dict:
            words_dict[lword] += 1
        else:
            words_dict[lword] = 1
    return words_dict

def tf(fn):
    doc_tf[fn] = {}
    maxfreq = 0
    for word,num in doc_words[fn].items():
        if maxfreq < num:
            maxfreq = num
    for word,num in doc_words[fn].items():
        #doc_tf[fn][word] = 1+math.log(num, 10)
        doc_tf[fn][word] = 0.5+0.5*(num/maxfreq)
        #/doc_numwords[fn]
    
def idf():
    doc_idf = {}
    for name,num in all_words.items():
        corpa_idf[name] = math.log(docs/num, 10)

def tfidf(fn):
    if not fn in doc_tf:
        tf(fn)
    if corpa_idf == {}:
        idf()
    for fn,words in doc_tf.items():
        doc_tfidf[fn] = {}
        for word,num in words.items():
            doc_tfidf[fn][word] = num * corpa_idf[word]

#for i in range(50):
#    fn = "corpa/dkbibel-txt/01_" + str(i + 1).zfill(2) + ".html"


directory = sys.argv[1]
filename = sys.argv[2]

for fn in os.listdir(directory):
    #if not fn.endswith(".html"):
    #    continue
    fn = directory + fn
    d = frequency(fn)
    doc_numwords[fn] = 0
    for word,freq in d.items():
        if word in all_words:
            all_words[word] += freq
        else:
            all_words[word] = freq
        doc_numwords[fn] += 1
        docs += 1
        doc_words[fn] = d
                

tfidf(filename)
                
words_sorted = OrderedDict(sorted(doc_tfidf[filename].items(), key = lambda t: t[1]))
print(words_sorted)

print(len(sys.argv))
