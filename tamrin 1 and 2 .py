import requests
from bs4 import BeautifulSoup
import json

#setting user agent and header
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
header = {'User-Agent': user_agent}
#retrieving xml file
url = 'https://sahmeto.com/crypto-sitemap.xml'
response = requests.get(url , headers= header)
#print(response.text)

#parsing the xml
soup = BeautifulSoup(response.text , 'lxml-xml')
#print(soup.find('url'))

# xml to dictionary
data = {'urlset':[]}
for url in soup.find_all('url'):
    attributes = {}

    #adding a field for tag name
    attributes['_tag'] = 'url'
    for tag in url:
        attributes[tag.name] = tag.text
        
    data['urlset'].append(attributes)
#print(data['urlset'][0:5])

# dictionary to json
json_string = json.dumps(data)

# creating a json file
with open('json_data.json', 'w') as file:
    file.write(json_string)
