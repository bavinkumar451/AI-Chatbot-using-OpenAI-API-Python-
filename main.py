from openai import OpenAI

client = OpenAI(api_key="sk-proj-ppchZ27ncoA54wG7LZEzaB7ksFFjo0fvrj_Ex8BAkO5scZP6btZmOAUYs5qXkgpP3Z")

def generate_response(prompt):
    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt
    )
    return response.output_text

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Chatbot:", generate_response(user_input))

