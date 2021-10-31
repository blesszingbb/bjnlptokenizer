# Sample Sentence: The wolf said: “Little pig, little pig, let me come in. "
# Sentence is either Sentence or Line Tokenized see code
# Importing word tokenizer from NLTK

from nltk.tokenize import word_tokenize, sent_tokenize, LineTokenizer
 
txt = '''The wolf said : " Little pig , little pig , let me come in . "'''

tokenized_text1 = sent_tokenize(txt)

print ("This is Sentence Tokenize: \n" )
print(tokenized_text1 )
print ("========================\n")

tokenized_text2 = LineTokenizer().tokenize(txt)
print ("This is Line Tokenize call: \n" )
print(tokenized_text2)
print ("========================\n")
