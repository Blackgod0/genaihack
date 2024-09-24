import requests

# Hugging Face API Key
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer HF_API_KEY"}

def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    image = response.content
    return image

prompt = "cat"
image = generate_image(prompt)

# Save image to file
with open("generated_image.png", "wb") as f:
    f.write(image)
print("Image saved as generated_image.png")
