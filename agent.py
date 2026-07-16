from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()
system_prompt = "Before every response print banana"
conversation =[]

while True: 
    user_input = input("user- ")
    if user_input == 'Quit':
        break
    
    conversation.append({"role":"user",
                         "content":user_input})
    
    response  = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=conversation,
        system = system_prompt
    )

    claude_reply = response.content[0].text

    conversation.append({"role":"assistant",
                         "content":claude_reply})
    
    print(claude_reply)