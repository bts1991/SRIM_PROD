import pandas as pd
import requests

url = 'https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&download=true'
headers = {
    "User-Agent":
    "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"
}

data = requests.get(url, headers=headers)
# ticker = pd.DataFrame(data.json()['data']['rows'])
# print(ticker)
# print(data)