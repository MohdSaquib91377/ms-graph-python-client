# Define imports
from email import header
import requests
from decouple import config

# Copy access token and dpecify ms GRAPH API endpoint you want to call, e.g. http://graph.microsoft.com/v1.0/groups/ to get all groups in your orgnizations
def request_to_client(access_token,endpoint):
    print(access_token)
    url = config("GRAPH_API_BASE_URL") + endpoint
    headers = {
        'Authorization': access_token
    }

    # Make GET request to the provided url passing the access token in the headers
    graph_result = requests.get(url = url, headers = headers)
    return graph_result.json()