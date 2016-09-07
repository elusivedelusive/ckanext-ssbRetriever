import requests

query = '''{
  "query": [
    {
      "code": "Region",
      "selection": {
        "filter": "item",
        "values": [
          "1103"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat"
  }
}'''

ssbRequest("http://data.ssb.no/api/v0/no/table/08921", query)
def ssbRequest(url, query):
    headers = {
        'cache-control': "no-cache",'postman-token': "ac843960-7be0-f3e5-776f-9e6d7ebb98fe"}
    response = requests.request("POST", url, data=query, headers=headers)
    print(response.text)
