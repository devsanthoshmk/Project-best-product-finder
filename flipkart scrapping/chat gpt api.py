import openai

# Set your API key
openai.api_key = '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'

# Provide the prompt text
prompt_text = "Once upon a time,"

# Call the completion API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt_text,
    max_tokens=50
)

# Get the generated completion
completion_text = response.choices[0].text.strip()

# Print the generated completion
print("Generated text:", completion_text)
import openai

# Set your API key
openai.api_key = 'YOUR_API_KEY'

# Provide the prompt text
prompt_text = "Once upon a time,"

# Call the completion API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt_text,
    max_tokens=50
)

# Get the generated completion
completion_text = response.choices[0].text.strip()

# Print the generated completion
print("Generated text:", completion_text)
