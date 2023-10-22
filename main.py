# Import the requests module
from bs4 import BeautifulSoup
import requests
import json


with open("./SF Doc/login.json") as login_file:
  content = login_file.read()
document = json.loads(content)

with open("./SF Doc/config.json") as login_file:
  content = login_file.read()
user = json.loads(content)

document['login']['payload']['username']    = user['username']
document['login']['payload']['pw']          = user['pw']
document['login']['payload']['oauth_token'] = user['oauth_token']

# Make a GET request with a tuple as the auth argument
#response = requests.get(url, auth=(username, password))
#response = requests.get(url)

payload = document['login']['payload']

#Create Request Session
with requests.session() as s:
    # Post to login
    rp = s.post(document['login']['headers']['Request URL'], data = payload)
    print("Response: ", rp.status_code)
    # Get to access data after login
    rg = s.get(document['login']['headers']['Request URL'])
    print("Response: ", rg.status_code)
    html = rg.text
    # Create a BeautifulSoup object from the HTML
    soup = BeautifulSoup(html, "html.parser")
    # Find the first <h1> tag in the HTML
    h1 = soup.find("h1")
    print(h1.text)
   

# Make POST
response = requests.post(document['login']['headers']['Request URL'], data = payload)

# Print the status code and the content of the response
print("Response: ", response.status_code)

html = response.text

# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, "html.parser")

# Find the first <h1> tag in the HTML
h1 = soup.find("h1")

# Print the text content of the <h1> tag
print(soup.text)

