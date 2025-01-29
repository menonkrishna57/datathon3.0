import requests

def generate_image(prompt, api_key):
    url = "https://api.leonardo.ai/generate"  
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "num_images": 1  
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json().get("image_url")  
    else:
        print("Error:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    api_key = input("Enter your Leonardo.ai API key: ")
    prompt = input("Enter the text prompt for the image: ")

    image_url = generate_image(prompt, api_key)

    if image_url:
        print("Successfully image generated! View image here:", image_url)