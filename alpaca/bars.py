import config, requests, json

# min_bars_url = '{}/5Min?symbols={}&limit=1000'.format(config.BARS_URL, 'AAPL,MSFT')
day_bars_url = '{}/day?symbols={}&limit=1000'.format(config.BARS_URL, 'AAPL,MSFT')

r = requests.get(day_bars_url, headers=config.HEADERS)
print(json.dumps(r.json(), indent=4))

