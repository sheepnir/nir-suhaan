import openai

user_prompt = input("Hey !!!, what is your promt? ")

# Setting up the authentiation with openai - set your api-key here
openai.api_key = ""


response = openai.Completion.create(
    model="text-davinci-003",
    prompt=user_prompt,
    temperature=1,
    max_tokens=128,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print(response["choices"][0]["text"])
