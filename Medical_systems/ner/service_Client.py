# !/usr/bin/env python
# _*_coding:utf-8_*_

#客戶端 ，用來呼叫service_Server.py
import socket
import sys
import struct
### Don't touch
def askForService(token,data):
    # HOST, PORT 記得修改
    global HOST
    global PORT
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    received = ""
    try:
        sock.connect((HOST, PORT))
        msg = bytes(token+"@@@"+data, "utf-8")
        msg = struct.pack(">I", len(msg)) + msg
        sock.sendall(msg)
        received = str(sock.recv(8096), "utf-8")
    finally:
        sock.close()
    return received
### Don't touch

def process(token,data):
    # 可在此做預處理

    # 送出
    result = askForService(token,data)
    
    return result

import json
global HOST
global PORT
HOST, PORT = "140.116.245.151", 9921
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJ2ZXIiOjAuMSwiaWF0IjoxNjYzMjUxMTg1LCJ1c2VyX2lkIjoiNDM4IiwiaWQiOjQ5Niwic2NvcGVzIjoiMCIsInN1YiI6IiIsImlzcyI6IkpXVCIsInNlcnZpY2VfaWQiOiIyIiwiYXVkIjoid21ta3MuY3NpZS5lZHUudHciLCJuYmYiOjE2NjMyNTExODUsImV4cCI6MTY5NDc4NzE4NX0.Bak8DleQBCzTSJP--DozFIG46zjaSKHArMie0kGc4uOxJJoduiMYQ1HchKdBz5ey4pZSNYzSXvprYLm458bQDu1pw5ZULUdPqE6tZv74EmZu_t5I6ANz-s3cxOgN-0zysBOtvM6S1MapRxd4Bv5t00blWPrxJ4wVcA46qS3E1JY"


data = '鄭鈞睿跟楊蒝麟一起被警察抓進監獄裡下棋，輸的明天被許顥議跟我肛'
#〔即時新聞／綜合報導〕美國參議院外交委員會14日通過《台灣政策法》（Taiwan Policy Act of 2022）,象徵美中台關係的重大轉變,美國國務院發言人普萊斯（Ned Price）在今天記者會上對此做出回應。
#在會中有記者詢問,美國參議院外交委員會通過《台灣政策法》,是否會進一步損害美中關係。若所創立的企業需有英文名稱，則尚需辦理「英文名稱預查」。
#'''
result = process(token,data)
#print(result)
res = json.loads(result)
reslist = res['wsResult']
Na, Nb, Nc, Nd = ([] for i in range(4))
# print(type(reslist[0]['pos']))

for i in reslist:
    if i['pos'] == 'Na':
        Na.append(i['word'])
    if i['pos'] == 'Nb':
        Nb.append(i['word'])
    if i['pos'] == 'Nc':
        Nc.append(i['word'])
    if i['pos'] == 'Nd':
        Nd.append(i['word'])
    

print('What:')
print(Na)
print('Who:')
print(Nb)
print('Where:')
print(Nc)
print('When:')
print(Nd)
print('Event:')
print(res['fullEventList'])
