import openai

#Put your key:
openai.api_key = 'sk-HbWsgb1---------'

def chat_completion(prompt):
    # Define the prompt for the chat-based completion
    prompt = f"You are a helpful assistant.\n\nUser: {prompt}\nAssistant:"

    # Call the OpenAI API for chat-based completion using OpenAI API v1.0.0
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose other engines like text-davinci-003
        prompt=prompt,
        max_tokens=150  # Adjust max_tokens as needed
    )

    # Extract the assistant's reply from the API response
    assistant_reply = response['choices'][0]['text'].strip()
    return assistant_reply

# Example usage
user_input = "The Capital of Egypt is ...."
response = chat_completion(user_input)
print(f"User: {user_input}\nAssistant: {response}")

