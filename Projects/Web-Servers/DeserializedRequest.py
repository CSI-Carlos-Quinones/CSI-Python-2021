import json, ssl
import urllib.request
from RandomHipsterStuff import RandomHipsterStuff


ssl._create_default_https_context = ssl._create_unverified_context

hipUrl = "https://random-data-api.com/api/hipster/random_hipster_stuff?size=100"

hipWords:RandomHipsterStuff = []

req = urllib.request.Request(hipUrl)

requestData = json.loads(urllib.request.urlopen(req).read())

for x in range(0,1000):
    for r in requestData:  
        # Deserialize 
        hipsterWord:RandomHipsterStuff = RandomHipsterStuff(**r)
        # Add object to list
        hipWords.append(hipsterWord)
        # Print id
        print(hipsterWord.words)

