# Sample text: ’This Is the Beat Generation: New York-San Francisco-Paris'


# Importing word tokenizer from NLTK
from nltk.tokenize import word_tokenize, regexp_tokenize
import regex, re

# The text title
book_title = "This Is the Beat Generation: New York-San Francisco-Paris"

#normal python built-in function
itokens = book_title.split()
#print(itokens)

# Tokenize using regular expression
atokens = re.split('[:-]', book_title)
print ("This is first tokenized Sentence using Regex - regular expression: \n" )
print(atokens)
print ("========================\n")

# Tokenize using nltk package


tokens = tokenized_text = word_tokenize(book_title)
print ("This is word tokenized using nltk package: \n" )
print(tokens)
print ("========================\n")

reg_pattern1 = '(\\w+|\\-?:?|)'
reg_pattern2 = '(\\w+|\\-:|)'

tokens1 = regexp_tokenize(book_title, reg_pattern1)
tokens2 = regexp_tokenize(book_title, reg_pattern2)
print ("This is 1st tokenized Sentence using Regex - nltk package: \n" )
print(tokens1)
print ("========================\n")

print ("This is 2nd tokenized Sentence using Regex - nltk package: \n" )
print(tokens2)
