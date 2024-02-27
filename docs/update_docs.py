import requests

response = requests.get("s3://openapi-docs-news/openapi.json")

with open("docs/openapi.json", "w") as file:
    file.write(response.text)