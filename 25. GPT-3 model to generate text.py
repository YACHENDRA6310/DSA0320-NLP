from transformers import pipeline

# Create the text generation pipeline using GPT-2
generator = pipeline('text-generation', model='gpt2', framework='pt')

def generate_text(prompt, max_length=100):
    response = generator(prompt, max_length=max_length, num_return_sequences=1)
    return response[0]['generated_text']

# Test the function
prompt = "Do you know India"
generated_text = generate_text(prompt)
print(f"Generated Text: {generated_text}")
