# Sample Sentence: ’The receptor-ligand complexes were then released from the cell membrane preparation ’ +\ ’by incubation with RIB + detergent, which contained ...
# Tasks to perform: - Tokenize using regular expression, - Tokenize using nlt package
# and For each tokenization, compute the number of tokens, using the len() function, and print the result.


# Importing word tokenizer from NLTK

from nltk.tokenize import word_tokenize, regexp_tokenize
import regex, re

# The text
txt = "The receptor-ligand complexes were then released from the cell membrane preparation ’ +\ ’by incubation with RIB + detergent, which contained RIB appended with 50 mM ’ +\ ’N-dodecyl-N, N (dimethylammonio) butyrate, 1.5% glycerol, and 2% NP-40 for 1 h at 37C’ +\ ’and centrifuged at 95,000 rpm for 3 h at 15C."

print("This is the main Text." )
print("========================\n")

print(txt + "\n")


#normal python built-in Split function
itokens = txt.split()
print ("Using normal python built-in split function : \n" )
print(itokens)
print ("No. of Tokens is =  " )
print (len(itokens))
print ("========================\n")

# Tokenize using regular expression
atokens = re.split('\W', txt)
print ("This is first tokenized Sentence using Regex - regular expression: \n" )
print(atokens)
print ("No. of Tokens is =  " )
print (len(atokens))
print ("========================\n")

print ("OR\n")
atokens1 = re.split('\W+', txt)
print(atokens1)
print ("No. of Tokens is =  " )
print (len(atokens1))
print ("========================\n")

# Tokenize using nltk package


tokens = tokenized_text = word_tokenize(txt)
print ("This is word tokenized using nltk package: \n" )
print(tokens)
print ("No. of Tokens is =  " )
print (len(tokens))
print ("========================\n")

reg_pattern1 = '(\\w+|\\+?%?|)'
reg_pattern2 = '(\\w+)'

tokens1 = regexp_tokenize(txt, reg_pattern1)
tokens2 = regexp_tokenize(txt, reg_pattern2)
print ("This is 1st tokenized Sentence using Regex - nltk package: \n" )
print(tokens1)
print ("No. of Tokens is =  " )
print (len(tokens1))
print ("========================\n")

print ("This is 2nd tokenized Sentence using Regex - nltk package: \n" )
print(tokens2)
print ("No. of Tokens is =  " )
print (len(tokens2))
print ("========================\n")


