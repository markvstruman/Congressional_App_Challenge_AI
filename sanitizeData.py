#import string
#import nltk
#import spacy
#import sys
import pandas as pd
#import wordcloud
#import lexical_diversity
#import re
#import collections
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
from wordcloud import WordCloud
from lexical_diversity import lex_div as ld
import os

#fileCount = 0
#directory = 'articles'
#for fileName in os.listdir(directory):
#    f = os.path.join(directory, fileName)
#    if os.path.isfile(f):
#        for 
def countWordFrequency(pathInput):
    ps = PorterStemmer()
    replacements = [",", ".", ":", "'", '"', "!", "?", "." ";", "@", "{", "}", "[", "]", "(", ")", "/", "#", "*", "_", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "%", "-", "£", "$", "&"]
    for i in range(0,72):
        text = ""
        frequencies = {}
        f = open("articles/article%d.txt" % i, 'r', encoding="utf-8")
        text = str(f.read()).lower()
        f.close()
        for r in range(0, len(replacements)):
            text = text.replace(replacements[r], " " + replacements[r] + " ")
        text = text.split()
        text = [word for word in text if len(word) < 12]
        for word in text:
            word = ps.stem(word)
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
        sortedD = sorted(frequencies, key=frequencies.get)
        sortedFrequencies = {}
        for key in sortedD:
            sortedFrequencies[key] = frequencies[key]
        f = open("cleanedArticles\Article%d.txt" % i, "w", encoding="utf-8")
        f.write(str(sortedFrequencies).replace(', ',',\n '))
        f.close()
    return sortedFrequencies

print(countWordFrequency('cleanedArticles/article0.txt'))
