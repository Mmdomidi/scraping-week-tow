import requests
import json
from pymongo import MongoClient

#setting the header
url ="https://api.stocktwits.com/api/2/streams/suggested.json?filter=top&limit=20&max=575263496"
header = {
  "authority": "api.stocktwits.com" ,
   "accept": "application/json" ,
   "accept-language": "en-GB,en-US;q=0.9,en;q=0.8" ,
   "authorization": "OAuth c72e98bd73bdbdbb29f9eee6bc2a66d2d1ec0b64" ,
   "origin": "https://stocktwits.com" ,
   "referer": "https://stocktwits.com/" ,
   "sec-ch-ua": '^\^"Not_A Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"109^\^", ^\^"Chromium^\^";v=^\^"109^\^"' ,
   "sec-ch-ua-mobile": "?0" ,
   "sec-ch-ua-platform": '^\^"Windows^\^"' ,
   "sec-fetch-dest": "empty" ,
  "sec-fetch-mode": "cors" ,
   "sec-fetch-site": "same-site" ,
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
#get json file
response = requests.get(url , headers = header)
json_data = response.json()

#connect to container
client = MongoClient('mongodb://localhost:27017')

#create a database called stocktwits
database = client['stocktwits']
#create a collection called messages
collection = database['messages']
#add messages from json file to the collection
for message in json_data.get('messages'):
  collection.insert_one(message)
client.close()
