import base64
import json
import requests

def main():
    aheaders = {'Content-Type': 'application/json'}
    url = "http://47.102.118.1:8089/api/challenge/submit"
    try:
        values = {
            "uuid": "f4b8b63a-3e80-4aad-8ba8-6889b8adf067",
            "teamid": 37,
            "token": "6098546f-f027-4a28-bacf-fda5805d21cf",
            "answer": {
                "operations": "dwwd",
                "swap": []
            }
        }

        request = requests.post(url, headers=aheaders, data=json.dumps(values))
        # html = urllib.request.urlopen(request).read().decode('utf-8'))
        print(json.loads(request.text))
    except Exception as err:
        print(err)


main()
