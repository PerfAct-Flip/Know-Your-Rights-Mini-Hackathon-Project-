import openai

with open("data.txt","r") as f:
    file_read = f.readlines()

file_read_string = ""
for string in file_read:
    file_read_string+=(str(string))
def get_openairesponse(openai_key_string, query_string):
    openai.api_key = openai_key_string
    query = {"role":"user","content":query_string}
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[query])
    chat_response = chat.choices[0].message.content
    return chat_response

question = input("What do you want to ask?: ")
query = "Here is some background info: "+file_read_string+". Based on this and add more, answer the question "+question

p = get_openairesponse('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',query)
print(p)