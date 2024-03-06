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


