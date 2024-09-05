from transformers import pipeline
from datasets import load_metric

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Define your texts (inputs for summarization)
texts = [
    "Artificial intelligence is transforming the way we live and work, making processes faster and more efficient.",
    "The concept of quantum computing leverages the principles of quantum mechanics to perform calculations at speeds unachievable by classical computers."
]

# Define your reference summaries (expected human-written summaries)
references = [
    "AI is changing work and life, making things faster and more efficient.",
    "Quantum computing uses quantum mechanics for extremely fast calculations, surpassing classical computing."
]

# Function to determine dynamic max_length based on input length
def get_max_length(input_text, ratio=0.3, min_length=10):
    """
    Determines the max length of the summary as a fraction of input length.
    Ensures max_length is at least the min_length.
    """
    input_length = len(input_text.split())
    max_length = max(int(input_length * ratio), min_length)
    return max_length

# Load the ROUGE metric
rouge = load_metric('rouge')

# Experiment with different prompt types
prompts = {
    "basic": "Summarize the following text: {}",
    "detailed": "Please provide a concise and informative summary of the following article, highlighting the main points and key insights: {}",
    "length-specific": "Summarize the following text in no more than 3 sentences: {}"
}

# Store the results
results = {}
summaries_by_prompt = {}

# Summarize with different prompts and evaluate ROUGE
for prompt_name, prompt in prompts.items():
    summaries = []
    
    for text in texts:
        # Get dynamic max_length
        max_len = get_max_length(text)
        
        # Apply the prompt to each text
        prompt_input = prompt.format(text)
        
        # Generate the summary with adjusted max_length
        summary = summarizer(text, max_length=max_len, min_length=10, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    
    results[prompt_name] = summaries
    summaries_by_prompt[prompt_name] = summaries

# Evaluate summaries with ROUGE and print both summaries and scores
for prompt_name, summaries in summaries_by_prompt.items():
    # Print the summaries for each prompt
    print(f"\nSummaries for {prompt_name} prompt:")
    for i, summary in enumerate(summaries):
        print(f"Text {i+1}: {summary}")
    
    # Calculate ROUGE scores
    scores = rouge.compute(predictions=summaries, references=references)
    
    # Print ROUGE scores for each prompt
    print(f"\nROUGE scores for {prompt_name} prompt:")
    print(f"ROUGE-1: {scores['rouge1'].mid.fmeasure:.4f}")
    print(f"ROUGE-2: {scores['rouge2'].mid.fmeasure:.4f}")
    print(f"ROUGE-L: {scores['rougeL'].mid.fmeasure:.4f}")
