# Define imports
import msal
from decouple import config
from helpers import request_to_client

# Enater tha details of AAP app registration
client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')
authority = f"https://login.microsoftonline.com/{config('TENANT_ID')}"
scopes = ["https://graph.microsoft.com/.default"]

# Create an MSAL instance provide tha client id, authority and client_credentials parameters
client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential= client_secret)

# sourc https://medium.com/@marian.reha/query-ms-graph-api-in-python-e8e04490b04e

# First, try to access the token in cache
token_result = client.acquire_token_silent(scopes,account=None)

# if token is available in cache then save it to in a variable
if token_result:
    access_token = f"Bearer {token_result['access_token']}"
    print('Access token loaded from chache')

# if the token is not loaded in cache then, acquire new one  from azure AD and save it in variable 
if not token_result:
    token_result = client.acquire_token_for_client(scopes = scopes)
    access_token = f"Bearer {token_result['access_token']}"
    print('New access token was acquired from Azure AD')

result = request_to_client(access_token,'users')
print(result)

