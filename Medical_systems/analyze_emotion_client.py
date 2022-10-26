import requests

def askForService(query:str, token:str) -> dict:
    '''
    Do sentiment analysis
    '''
    response = requests.post("http://140.116.245.157:9526", data={"inputtext":query, "token":token})
    if response.status_code == 200:
        return {"status":True, "result": response.text.strip()}
    else:
        return {"status":False, "result": None}
    



if __name__ == "__main__":
    query = "基督思想好無聊"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJ2ZXIiOjAuMSwiaWF0IjoxNjY0ODU1NzYwLCJ1c2VyX2lkIjoiNDM4IiwiaWQiOjU2Mywic2NvcGVzIjoiMCIsInN1YiI6IiIsImlzcyI6IkpXVCIsInNlcnZpY2VfaWQiOiIzMCIsImF1ZCI6IndtbWtzLmNzaWUuZWR1LnR3IiwibmJmIjoxNjY0ODU1NzYwLCJleHAiOjE4MjI1MzU3NjB9.e7MdxzPQnGB99cyFEcDKfG7imkOIrSkY8S8ClVBQQq-gFpobJIuiG87-Q-GR6-nVawxzPVLf5lkb7rjD4LrajDs30A5cA_5LxveJE9e3Okfrvx0WdIC8MIaPD2rJGlnExtM_R7P36KV-Ng6JVrja7hJ5ocIKRjqrPxcvFbAFGPM"
    r = askForService(query, token)
    print(r['result'])
