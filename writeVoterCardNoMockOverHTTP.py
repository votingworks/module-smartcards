
import json, hashlib, time, http.client

short_value = json.dumps({"t":"voter","bs":"2","pr":"6522","c": round(time.time())})

client = http.client.HTTPConnection('localhost', 3001)
client.request('POST', '/card/write-no-mock', short_value)
response = client.getresponse()
print(response.read().decode('utf-8'))
