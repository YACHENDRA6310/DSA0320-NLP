from nltk.corpus import wordnet as wn
import nltk

word = "bank"
synsets = wn.synsets(word)

print(f"Synsets for the word '{word}':")
for syn in synsets:
    print(f"{syn.name()} - {syn.definition()}")
            
if synsets:
    print(f"\nExamples for the first synset '{synsets[0].name()}':")
    print(synsets[0].examples())
 
