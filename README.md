# song-recommendor

## Libraries
<strong>Python Version: </strong>3.8<br>
<strong>Libraries: </strong>pandas, selenium, beautifulsoup, flask<br>

## How to use
<strong>Curl</strong>
```
curl -X GET https://sesankm-recommend-song.herokuapp.com/recommendc -H "Content-type:application/json" -d "{"input":"drake-gods plan"}"
```
Curl on windows:
```
curl -X GET https://sesankm-recommend-song.herokuapp.com/recommend -H "Content-type:application/json" -d "{\"input\":\"drake-gods plan\"}"
```

<strong>Python</strong>
```
import requests

url = "https://sesankm-recommend-song.herokuapp.com/recommend"
headers = {"Content-Type": "application/json"}
data = {"input": "Drake-gods plan"}

r = requests.get(url, headers=headers, json=data)

print(r.json)
```

* requests timeout after 30 seconds for heroku apps
* if this happens, you can run the code locally <br>
	[Download chromedriver version 87](http://chromedriver.chromium.org/downloads)
	```
	git clone https://github.com/sesankm/song-recommender
	pip install -r local_requirements.txt
	# copy chromedriver executable into the same directory git repo
	python recommend.py "drake-gods plan"
	```
