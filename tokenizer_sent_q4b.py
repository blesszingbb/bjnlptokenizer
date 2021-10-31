# Sample Sentence: Welcome! Can I help you? I’m fine.
# Sentence is either Line or Tab Tokenized see code
# Importing word tokenizer from NLTK

from nltk.tokenize import word_tokenize, LineTokenizer, TabTokenizer
txt = "Welcome! Can I help you? I’m fine."

tokenized_text = LineTokenizer().tokenize(txt)

print(tokenized_text)
print ("========================\n")

tokenized_text2 = TabTokenizer().tokenize(txt)

print(tokenized_text2)
print ("========================\n")

