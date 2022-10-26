from record import *
from taiwanese_tts import *
from chinese_stt import*
from gtts import gTTS
import os
from analyze_emotion_client import *

def ch_tts(answer):
	tts = gTTS(text = answer, lang = 'zh-tw')
	tts.save("responce.mp3")

def chatbot(question):
	f = open("questions.txt", encoding='utf-8')
	q = {}
	for line in f:
		try:
			l = line.split(":")
			q[l[0].strip()] = l[1].strip()
		except:
			print("oops")
	if question in q:
		return q[question]
	else:
		return "idk"

def main():
	token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3OTEyOTMxMzMsImlhdCI6MTYzMzYxMzEzMywi    c3ViIjoiIiwiYXVkIjoid21ta3MuY3NpZS5lZHUudHciLCJpc3MiOiJKV1QiLCJ1c2VyX2lkIjoiMjkwIiwibmJmIjoxNj    MzNjEzMTMzLCJ2ZXIiOjAuMSwic2VydmljZV9pZCI6IjI0IiwiaWQiOjM5Niwic2NvcGVzIjoiMCJ9.XtqCCNnmc6tiNIO    vcCsY6_vX-IjQFreYQWeU3BqXAvhZYCnjRUZvkcQcRLo-FjUikviipwRRYZhBGXK2Pd2xK8gfNu7LKRGh9V3sPvHIHn4Mx    C-YzV0tjQItGyIDW2w708YJQffx3v4A7wxnj3sjkxDxHIS8LApRcgk7Cd3Rdig"
	while 1:
		record() #saves to "recording.wav"
		question = chinese_recognize("recording.wav") + '?'
		print(question)	
		answer = chatbot(question)
		print(answer)
		print(emo(question))
		if answer != 'idk':
			lang = input("Chinese (c) or Taiwanese (t)?\n")
			if lang == 't':
				tw_tts(answer)
				os.system("aplay output.wav")
			if lang == 'c':
				ch_tts(answer)
				os.system("mpg123 responce.mp3")

if __name__ == '__main__':
	main()
	
