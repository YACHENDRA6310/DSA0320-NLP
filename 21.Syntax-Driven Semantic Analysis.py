import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk.corpus import wordnet

def get_meaning(word):
    return wordnet.synsets(word)[0].definition() if wordnet.synsets(word) else "No definition found"

def extract_noun_phrases(sentence):
    grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
    tree = RegexpParser(grammar).parse(pos_tag(word_tokenize(sentence)))
    return [" ".join(word for word, _ in subtree.leaves()) for subtree in tree.subtrees() if subtree.label() == "NP"]

def main():
    sentence = input("Enter a sentence: ")
    for phrase in extract_noun_phrases(sentence):
        meanings = {word: get_meaning(word) for word in phrase.split()}
        print(f"\nNoun Phrase: {phrase}\n" + "\n".join(f"  {word}: {meaning}" for word, meaning in meanings.items()))

if __name__ == "__main__":
    main()
