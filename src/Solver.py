import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import os


def get_keywords():
    outputFile = open('emailKeywords.json', 'w')
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, str(textToRead).encode(), headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')

        outputFile.write(data)

        jsonData = json.loads(data)
        phrases = jsonData['documents'][0]['keyPhrases']
        print(phrases)
        conn.close()
    except Exception as e:
        print("[Error {0}] {1}".format(e.args, e.args))

    return


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '136af33eef9c46fa9e3adc53632baf97',
}

params = urllib.parse.urlencode({})

emailBodyText = open('body_text.txt', 'r').read()

textToRead = {
  "documents": [
    {
      "language": "en",
      "id": "1",
      "text": emailBodyText
    }
  ]
}

print('Starting keyword extraction.')

get_keywords()

########################################################

'''
print('Starting topic detection')

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '136af33eef9c46fa9e3adc53632baf97',
}

params = urllib.parse.urlencode({})

allDataList = []
i = 0

for filename in os.listdir('dataset'):
    txt = open('dataset/' + filename, 'r').read()
    dic = {
          "language": "en",
          "id": str(i),
          "text": txt
        }
    allDataList.append(dic)
    i += 1

textToRead2 = {"documents": allDataList}

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/topics?%s" % params, str(textToRead2).encode(), headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    jsonData = json.loads(data)
    phrases = jsonData['documents'][0]['keyPhrases']
    print(phrases)
    conn.close()
except Exception as e:
    print("[Error {0}] {1}".format(e.args, e.args))
'''
