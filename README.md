# song-recommendor

## Libraries
<strong>Python Version: </strong>3.8<br>
<strong>Libraries: </strong>pandas, selenium, beautifulsoup, flask<br>

## How to use
<strong>Curl</strong>
```
curl -X GET https://sesankm-recommend-song.herokuapp.com/recommendmusic -H "Content-type:application/json" -d "{"input":"drake-gods plan"}"
```
Curl on windows:
```
curl -X GET https://sesankm-recommend-song.herokuapp.com/recommendmusic -H "Content-type:application/json" -d "{\"input\":\"drake-gods plan\"}"
```

<strong>Python</strong>
```
import requests

url = "http://127.0.0.1:5000/reccomendmusic"
headers = {"Content-Type": "application/json"}
data = {"input": "Drake-gods plan"}

r = requests.get(url, headers=headers, json=data)

print(r.json)
```