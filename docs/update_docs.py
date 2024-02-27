import requests

response = requests.get("http://localhost:8000/openapi.json")

with open("docs/openapi.json", "w") as file:
    file.write(response.text)