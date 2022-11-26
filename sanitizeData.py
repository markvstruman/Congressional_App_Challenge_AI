import pandas as pd
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

def countWordFrequency():
    # An object used for taking the root of a word, i.e. 'programming', 'programmer', programs' are turned into 'program'
    ps = PorterStemmer()
    # a list of characters that we want to seperate from text
    replacements = [",", ".", ":", "'", '"', "!", "?", "." ";", "@", "{", "}", "[", "]", "(", ")", "/", "#", "*", "_", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "%", "-", "£", "$", "&"]
    
    # 71 is abritrary, it's just the number of articles I was able to pull today
    # In the future, it would be wise to just use the number of articles in the /articles directory as the number to iterate through
    # We would then have to move the files out of the /articles and /cleanedArticles directories after processing
    for i in range(0,300):
        # A string to hold the contents of the article's contents when read
        text = ""
        # Created a dictionary mapping words to the number of their occurances
        frequencies = {}
        sortedFrequencies = {}

        # Opening the article file, assigning text it's contents, and closing the file
        f = open("articles/article%d.txt" % i, 'r', encoding="utf-8")
        text = str(f.read()).lower()
        f.close()

        # Going through each character we listed previously to create a space
        for r in range(0, len(replacements)):
            # Creating a space here allows us to count it in the dictionary later
            text = text.replace(replacements[r], " " + replacements[r] + " ")
        
        # Splitting the string of text into an array of words
        text = text.split()

        # I figure any word processed that's greater than 12 characters is a fluke
        # I.e. a link, or a piece of HTML data that escaped the parsing of newspaper3k
        text = [word for word in text if len(word) < 12]

        # For every word in the array...
        for word in text:
            # take the 'root' of the word with our PorterStemmer object...
            word = ps.stem(word)

            # if the word has been seen already, add one to the number of occurances...
            if word in frequencies:
                frequencies[word] += 1
            # if it's a new word, make a dictionary value to begin counting it
            else:
                frequencies[word] = 1
            
        # Sorting the frequencies dictionary so its ranked in ascending order
        sortedD = sorted(frequencies, key=frequencies.get)
        for key in sortedD:
            sortedFrequencies[key] = frequencies[key]

        # Opening the appropriately matching file in cleanedArticles directory
        f = open("cleanedArticles\Article%d.txt" % i, "w", encoding="utf-8")

        # Writing the sortedFrequencies dictionary to the file, line by line
        f.write(str(sortedFrequencies).replace(', ',',\n '))
        f.close()
    # Return statement useful for debugging
    return sortedFrequencies

countWordFrequency()
