import openai
import sys
from colorama import  Back, Style

if __name__ == '__main__':
    print("Passed System Arguments: " + str(sys.argv))
    if len(sys.argv) < 5:
        print("Usage: python3 api_call.py API_KEY paragraph_0.txt paragraph_1.txt paragraph_2.txt query.txt")
        sys.exit(1)
    openai.api_key = sys.argv[1]
    number_of_paragraphs = int(sys.argv[2])
    paragraphs_top = []
    query_para = []
    for i in range(3, 3+number_of_paragraphs//2):
        with open(sys.argv[i], 'r') as f:
            paragraphs_top.append(f.read())

    paragraphs_bottom = []
    for i in range(3+number_of_paragraphs//2, 3+number_of_paragraphs-2):
        with open(sys.argv[i], 'r') as f:
            paragraphs_bottom.append(f.read())

    with open(sys.argv[len(sys.argv)-1], 'r') as f:
        paragraphs_top.append(f.read())
        paragraphs_bottom.append(f.read())
    
    with open(sys.argv[len(sys.argv)-2], 'r') as f:
        query_para.append(f.read())
    
    paragraphs_top = '\n'.join(paragraphs_top)
    paragraphs_bottom = '\n'.join(paragraphs_bottom)
    query_para = '\n'.join(query_para)
    print("\033[31m"+"Sending Preliminary Query to ChatGPT: "+"\033[30m")
    print()
    #print(paragraphs_top)
    query_top = {
        "role": "user", "content": paragraphs_top
    }
    query_bottom = {
        "role": "user", "content": paragraphs_top
    }
    chat_top = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[query_top]
    )
    print("\033[35m"+"Preliminary Processed"+"\033[30m")
    print()
    print("\033[32m"+"Sending more Context to ChatGPT: "+"\033[30m")
    print()
    #print(paragraphs_bottom)
    chat_bottom = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[query_bottom]
    )
    print("\033[35m"+"Context Query Processed"+"\033[30m")
    print()
    print("\033[34m"+"Do you wish to print the processed queries? (Enter 0 for NO and 1 for YES):"+"\033[30m")
    print()
    choice = int(input())
    if(choice==1):
        print(chat_bottom.choices[0].message.content)
        print(chat_top.choices[0].message.content)
    print()
    reply_top = chat_top.choices[0].message.content
    reply_bottom = chat_bottom.choices[0].message.content
    
        
    final_paragraph =    f'''Here are two excerpts for you to consider. Higher Priority: '''+reply_top+''' 
    Lower Priority: '''+reply_bottom+'''
      . Use it to answer the question and give the answer in about 500 words. Use these excerpts: '''+query_para
    print("\033[34m"+"Do you wish to use our GPT2 model for extra context in querying the LLM? (Enter 0 for NO and 1 for YES):"+"\033[30m")
    print()
    choice = int(input())
    if(choice==1):
        with open('gpt2.txt', 'r') as f:
            final_paragraph.append(f.read())
    query_final = {
        "role": "user", "content": final_paragraph
    }
    print("\033[33m"+"Sending Query to ChatGPT: "+"\033[30m")
    print()
    reply = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[query_final]
    )
    print("\033[31m"+"Here is the final answer: "+"\033[30m")
    print()
    print("\033[36m"+reply.choices[0].message.content+ "\033[30m")
    print()