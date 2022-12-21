import requests
import json
import easywebdav as w
from time import sleep
requests.adapters.DEFAULT_RETRIES = 9999999999999
def main():
    re=requests.get("https://api.lolicon.app/setu/v2?size=original&excludeAI=true")
    re=json.loads(re.text)
    print(str(re))
    name=str(re['data'][0]['pid'])
    re=re['data'][0]['urls']['original']
    name=name+".jpg"
    print(str(re))
    w.basestring = str
    w.client.basestring = str
    u=w.connect("app.koofr.net",username="admin@kandk.cf",password="0u30 l4px b1r1 heag",protocol='https')
    png=requests.get(re).content
    with open(name, 'wb') as f:
            f.write(png)
    print("Saved "+name,end="\n")    
    u.upload(name,"dav/tt/apipic/"+name)
    print("\n")
while True:
  try:
    main()
  except:
    while True:
      print("Connection refused by the server..")
      print("Let me sleep for 5 seconds")
      print("ZZzzzz...")
      sleep(5)
      print("Was a nice sleep, now let me continue...")
      continue