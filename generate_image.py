import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

topic = input("Enter a topic for the image: ")
user_prompt = f"A detailed, realistic image illustrating the topic: {topic}."

try:
    print(f"Generating image with prompt: '{user_prompt}'")
    response = client.images.generate(
        model="dall-e-3",  # Use your DALL-E deployment name
        prompt=user_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    print("\n✅ Image successfully generated!")
    print(f"Image URL: {image_url}")

except Exception as e:
    print(f"❌ An error occurred: {e}")