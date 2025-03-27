import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

client = AzureChatOpenAI(
    azure_endpoint = os.getenv("apiBase"),
    api_key=os.getenv("apiKey"),
    api_version=os.getenv("apiVersion"),
    azure_deployment=os.getenv("modelName"))

try:
    response1 = client.invoke('what is AI')
    print(response1.content)
    response2 = client.invoke(f'based on above response {response1.content} what can I do with it')
    print(response2.content)
except Exception as e:
    print(e)
