import requests

url = "http://127.0.0.1:5000/generate"
payload = {
    "prompt": "lion playing with ball"
}

print("🔁 Sending request...")
response = requests.post(url, json=payload)

try:
    data = response.json()
    print("✅ Response received!")
    print(data)
except Exception as e:
    print("❌ Failed to decode response:", response.text)
