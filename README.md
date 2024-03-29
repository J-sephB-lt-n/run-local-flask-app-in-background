# run-local-flask-app-in-background
Code illustrating how to locally host a Flask app in the background (e.g. for automated endpoint testing)

```bash
$ pip install -r requirements.txt
```

```python
# main.py
import requests
from background_localhost import BackgroundLocalHost

with BackgroundLocalHost(app_name="test_app", port=8000):
    endpoint_response = requests.get("http://localhost:5000/health_check")
    print(endpoint_response, endpoint_response.text)

# check that the background flask app has been killed correctly by the context manager #
try: 
    endpoint_response = requests.get("http://localhost:8000/health_check")
    print(endpoint_response, endpoint_response.text)
except requests.exceptions.ConnectionError:
    print("ERROR: cannot connect to http://localhost:8000/health_check")
```

```bash
$ python main.py
hosting local flask app 'test_app' on port 8000
127.0.0.1 - "GET /health_check HTTP/1.1" 200 -
<Response [200]> Endpoint is working
killed local flask app 'test_app' on port 8000
ERROR: cannot connect to http://localhost:8000/health_check 
```
