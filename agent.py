from dotenv import load_dotenv #is a function which helps to fetch the keys that are stored in .env file
from datetime import datetime

load_dotenv()
client = Anthropic() #Calling this pre-defined object and storing in variable called client.
conversation=[]

def getDatetime():
    return str(datetime.now())

tools = [
{
    "name": "getDatetime",
    "description": "fetches date and time",
    "input_schema":{
        "type": "object",
        "properties": {},
        "required": []

}
}
]

while True:
    
    user_input= input("You :")

    if user_input.lower()== "quit":
        break

    conversation.append({"role": "user", "content": user_input})
    response = client.messages.create(
    model = "claude-opus-4-5",
    max_tokens = 1024,
    messages = conversation,
    tools = tools
    )

    if response.content[0].type == "text":
        print(response.content[0].text)
        conversation.append({"role":"assistant", "content":response.content[0].text})

    else:
        tool_name =response.content[0].name
        
        if tool_name == "getDatetime":
            
            tool_result= getDatetime()

            conversation.append({"role": "assistant", "content": response.content})

            conversation.append({
                "role": "user",
                "content":[
                    {
                        "type": "tool_result",
                        "tool_use_id": response.content[0].id,
                        "content": tool_result
                    }
                ]
                })
                
                
            response = client.messages.create(
                    model = "claude-opus-4-5",
                    max_tokens = 1024,
                    messages = conversation,
                    tools= tools
                )
                
                
            print(response.content[0].text)
            conversation.append({"role": "assistant", "content": response.content[0].text})