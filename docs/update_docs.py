#!/usr/bin/env python
import os
import requests

# Replace 'localhost:8000' with the actual host and port of your FastAPI application
base_url = 'http://localhost:8000'
openapi_path = '/openapi.json'
docs_save_path = "./docs/"
url = base_url + openapi_path

try:
    response = requests.get(url)
    response.raise_for_status()
    with open(os.path.join(docs_save_path, 'openapi.json'), 'wb') as f:
        f.write(response.content)
    print('OpenAPI JSON downloaded successfully.')
except requests.exceptions.RequestException as e:
    print(f'Error downloading OpenAPI JSON: {e}')
