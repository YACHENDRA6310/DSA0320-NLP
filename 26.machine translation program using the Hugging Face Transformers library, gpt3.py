from transformers import pipeline
translator = pipeline("translation_en_to_fr")
while True:
    english_text = input("Enter English text to translate to French (or type 'exit' to quit): ")
    if english_text.lower() == 'exit':
        break
    translation = translator(english_text, max_length=40)
    french_text = translation[0]['translation_text']
    print('French:', french_text)
