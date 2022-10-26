import requests
import json

def request(sent, token):
    res = requests.post("http://140.116.245.157:2001", data={"data":sent, "token":token})
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        return None 


if __name__ == "__main__":
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJ2ZXIiOjAuMSwiaWF0IjoxNjYzMjUxMTkwLCJ1c2VyX2lkIjoiNDM4IiwiaWQiOjQ5Nywic2NvcGVzIjoiMCIsInN1YiI6IiIsImlzcyI6IkpXVCIsInNlcnZpY2VfaWQiOiIxIiwiYXVkIjoid21ta3MuY3NpZS5lZHUudHciLCJuYmYiOjE2NjMyNTExOTAsImV4cCI6MTY3ODgwMzE5MH0.W8OQ1-kf6otF9WPOy1Kbe6vemaX39vIQVpFP3KuKpWjsHO-ciYqoDJOkuWAlJP5-18S0x6W3pW7nivSzxIbZ8iguOK0gowUtW9uE3-Ov9CDGbdbREfZeGpvODdJR6WftC5gKE-LaKveAkYK9YOtzukxUCNYonYRCZ2hkVECGsZQ" # Go 'WMMKS API' website to get your token
    sent = '''一、有關企業開辦流程簡介整體而言，在我國要創立一家企業並正式營業，基本上應完成「公司、商業或有限合夥組織名稱預查」、「公司、商業或有限合夥組織登記」，並依規定完成「稅籍登記」（原名稱：營業登記）、「成立勞/健保投保單位」等4個主要程序。若所創立的企業需有英文名稱，則尚需辦理「英文名稱預查」；若所創立的企業有經營商品輸出入業務者則另需同時辦理「英文名稱預查」及「出進口廠商登記」；此外，如果所創立的企業僱用勞工人數超過30人以上需另外辦理「工作規則核備」。以下簡要說明前述各項程序：'''
    #"陳振皓跟洪翊碩還有柯享宇、涂旭含今天到安平的公園跟一群小朋友玩，很好玩"
    r = request(sent, token) #dict of lists of lists
    

    persons_table, locations_table, timings_table, objects_table, events_table = ([] for i in range(5))
    verb_pos_table=["VA","VAC","VB","VC","VCL","VD","VF","VE","VG","VH","VHC","VI","VJ","VK","VL","V_2"]
    endings_pos_table=["COMMACATEGORY","PERIODCATEGORY","QUESTIONCATEGORY","SEMICOLONCATEGORY"]

    #ner
    for i,j in list(zip(r['ws'][0],r['pos'][0])):
        if j == 'Nb':
            persons_table.append(i)
        elif j == 'Nc':
            locations_table.append(i)
        elif j == 'Nd':
            timings_table.append(i)
        elif j == 'Na':
            objects_table.append(i)

    #event
    i = 0
    while i < len(r['ws'][0]):
        if r['pos'][0][i] in verb_pos_table:
            event = ''
            while i < len(r['ws'][0]) and r['pos'][0][i] not in endings_pos_table:
                event += r['ws'][0][i]
                i = i+1
            events_table.append(event)
        i = i+1


    print('Persons:',persons_table)
    print('Locations:',locations_table)
    print('Timings:',timings_table)
    print('Objects:',objects_table)
    print('Events:',events_table)