from langcain_openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model="gpt-4",temperature=0,max_completion_tokens=1000)

model.invoke("What is the capital of pakistan?")

print(result)
print(result.content)

