from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained GPT-2 model and tokenizer
model_name = 'gpt2'  # You can also use 'gpt2-medium', 'gpt2-large', etc.
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Ensure the model is in evaluation mode (necessary for inference)
model.eval()

def generate_text(prompt, max_length=50):
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors='pt')

    # Generate text
    output = model.generate(
        inputs['input_ids'], 
        max_length=max_length, 
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True
    )

    # Decode the generated text
    text = tokenizer.decode(output[0], skip_special_tokens=True)
    return text


prompt = "The future of AI technology is"
generated_text = generate_text(prompt, max_length=100)
print(generated_text)
