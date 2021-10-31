# Create an input string like a story for instance
# Create a set of English Stopwords
# Removing Stopwords from word_tokens and inserting rest of the words in filtered sentence list using looping or list comprehension.

# Importing stopwords and word tokenize from NLTK.corpus and tokenize respectively

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# The Story
story = "Stop words are most common words found in any natural language which carries very little or no significant semantic context in a sentence. It just carry syntactic importance which aid in formation of sentence. As a preprocessing operation it must be removed to ease further task and speedup core task in text processing. Ibrahim A [3] conducted a comparative study on the effect of stop words elimination on Arabic Information Retrieval where three stop lists viz, General Stop list, corpus based stop-list and combined stop list were used for comparative study. General stop-list performed better than the rest of the two. Ashish T, et al [4] eliminated stop-word in Gujarati language by preparing frequency list from Gujarati corpus by analyzing popular Gujarati newspapers. Riyad A, et al [5], used Finite State Machine (FSM) algorithm to eliminate stop-words for Arabic Language. Basim A, et al [6] have designed and implemented a new stop-word removal technique for Arabic language based on dedicated list and algorithm which compares stopwords if it fulfills desired string length criteria. Vijayarani S, et al[7] used Zipf’s Law (Z method) for creation of stop-words. Rakholia and Saini [8] have presented a rule-based approach to dynamically identify stop words for Gujarati language. They have also deployed this approach with additional cosine similarity based Vector Space Model for information retrieval in Gujarati language [9]. Kaur J and Saini JR have presented the list of Punjabi stop words [10], its Partof-Speech class based classification [11] and its Gurumukhi and Shahmukhi script versions [12]. Saini and Rakholia [13] have presented an analytic in-depth report on continent and script-wise divisions-based statistical measures for stopwords lists of various international Languages."

#English stopwords
stop_words = set(stopwords.words('english'))

#Tokenize story
word_tokens = word_tokenize(story)


#Printing out Tokenize story
print("See Tokenized words list below:")
print ("=======================\n")
print (stop_words)
print ("=======================\n")
print ("See the No.# of words below:")
print ("=======================\n")
print (len(stop_words))
print ("=======================\n")

print("See Stop words list below:")
print ("=======================\n")
print (word_tokens)
print ("=======================\n")
print ("See the No.# of Stop words below:")
print ("=======================\n")
print (len(word_tokens))
print ("=======================\n")

# Removing Stopwords from word_tokens and inserting rest of the words in 
# filtered_sentence list using list comprehension.

filtered_sentence = [w for w in word_tokens if not w in stop_words]
print("See Tokenize words list below:")
print ("=======================\n")
print("Word Tokens : ", word_tokens)
print ("=======================\n")
print("See the NO.# of Stop words below:")
print ("=======================\n")
print (len(stop_words))
print ("=======================\n")

print("See Filtered Sentence list below:")
print ("=======================\n")
print("Filtered Sentence : ", filtered_sentence)
print ("=======================\n")
print("See the NO.# of Filtered Sentences below:")
print ("=======================\n")
print (len(filtered_sentence))
print ("=======================\n")
