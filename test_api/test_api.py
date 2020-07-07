import json
import requests

address = 'http://35.225.24.237'
data = {
    "text":"this is a beautiful day. World Cup will be taking place for Olympics in 2020 in Tokyo"
}
r = requests.post(address, json=data)
print(r.status_code)
print(r.text)
