import urllib
import json

url = "http://jsonplaceholder.typicode.com/"

response = urllib.urlopen(url)
data = json.loads(response.read())

print(data)
