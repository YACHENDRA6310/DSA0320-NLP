def calculate_cohesion_score(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    repeated_word_count = sum(count for count in word_counts.values() if count > 1)
    cohesion_score = repeated_word_count / len(words) if words else 0
    return cohesion_score
text = "This is a sample text. This text is an example of text."
cohesion_score = calculate_cohesion_score(text)
print(f"Cohesion score: {cohesion_score}")
