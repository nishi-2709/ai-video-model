from openai import AzureOpenAI
import base64

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://prash-mek4ic8o-eastus2.cognitiveservices.azure.com/",
    api_key="52aOCQ3h77sSKoIwJYHlb6fg3kA8AWuBag739EssIs6ka8JLhK8PJQQJ99BHACHYHv6XJ3w3AAAAACOGW8NA"
)

topic = input("Enter a topic: ")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that generates informative text on a given topic.",
        },
        {
            "role": "user",
            "content": f"Write a detailed and informative text about the topic: {topic}",
        }
    ],
    max_completion_tokens=16384,
    model="gpt-5-mini"
)

print(response.choices[0].message.content)