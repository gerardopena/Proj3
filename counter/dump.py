import sys
import requests
import json

# This does not work with on of the urls
url = str(sys.argv[1])
r = requests.get(url)

a_dict = json.loads(r.content)

for value in a_dict['keys']:
    url = str(sys.argv[1])
    new_url = url + '/' + str(value)
    
    r = requests.get(new_url)
    print(r.text)

#This is was provided
# url = sys.argv[-1] #getting the parameter passed in and setting it as a variable

# r = requests.get(url)
# temporary = r.json()
# the_values = temporary.values()

# for y in the_values:
#     for x in y:
#         place = requests.get(url + str(x))
#         print(place.json())
