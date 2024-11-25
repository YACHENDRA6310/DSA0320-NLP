import spacy
nlp = spacy.load("en_core_web_sm")

def resolve_references(text):
    """
    Resolves references (pronouns) within a given text using SpaCy.
    """
    doc = nlp(text)
    resolved_text = text
    
    for token in doc:
        if token.pos_ == "PRON" and token._.in_coref:
            referent = token._.coref_clusters[0].main
            resolved_text = resolved_text.replace(token.text, referent.text, 1)
    
    return resolved_text

def main():
    text = input("Enter a text: ")
    print("\nOriginal Text:\n", text)
    resolved_text = resolve_references(text)
    print("\nResolved Text:\n", resolved_text)

if __name__ == "__main__":
    main()
