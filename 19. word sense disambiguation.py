from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

sentence = "The bank can guarantee deposits will be safe."
ambiguous_word = "bank"

tokens = word_tokenize(sentence)

sense = lesk(tokens, ambiguous_word)

print(f"Best sense for '{ambiguous_word}': {sense.name()}")
print(f"Definition: {sense.definition()}")
