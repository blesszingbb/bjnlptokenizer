# Sample text: The wolf said: “Little pig, little pig, let me come in. "
# The text is  Word (17) and Space (11) Tokenized and has different number of tokens seen  see code

#Word Tokenization
# Importing word tokenizer from NLTK
from nltk.tokenize import word_tokenize, SpaceTokenizer

# Create an input title
msg = '''The wolf said: "Little pig, little pig, let me come in."'''

# breaking the title into word/space tokens and assigning it to a new variable.

tokenized_text = word_tokenize(msg)
tokenized_text1 = SpaceTokenizer().tokenize(msg)

# Printing the tokenized paragraph. It will return a list of tokens.

print("This is Word Tokenization")
print(tokenized_text)
print(len(tokenized_text))

print("This is Space Tokenization")
print(tokenized_text1)
print(len(tokenized_text1))
