# -*- coding: utf-8 -*-
"""f74096336_word_segmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ul5Ns2qtw0u7dULNFBUXC_qKTNiXP2sL
"""

import string
class SEG(object):
  def __init__(self, dic_path):
    self.dictionary = set()
    self.maximum = 0
  
    with open(dic_path, 'r', encoding='utf8') as f:
      for line in f:
        line = line.strip()
        if not line:
          continue
        self.dictionary.add(line)
        if len(line)>=self.maximum:
          self.maximum = len(line)

  def sentence_seg(self, text):
    result = []
    index = 0
    prev = 0
    while index < len(text):
      sentence = None
      if text[index] == '，' or text[index] == '。':
        sentence = text[prev:index+1]
        prev = index+1
        result.append(sentence)
      index += 1
    return result

  def word_seg(self, text):
    result = []
    index = 0
    while index < len(text):
      word = None
      while text[index] in string.ascii_letters:
        if word is None:
          word = text[index]
          index += 1
        else:
          word += text[index]
          index += 1
      if not word is None:
        result.append(word)
      for size in range(self.maximum, 0, -1):
        if index + size > len(text):
           continue
        piece = text[index:index + size]
        if piece in self.dictionary:
          word = piece
          result.append(word)
          index += size
          break
      if word is None:
        result.append(text[index])
        index += 1
    return result

def main():
  text = "聯合國教科文組織的簡稱是UNESCO，旨在通過教育、科學及文化來促進各國合作，對和平與安全作出貢獻。"
  tokenizer = SEG('dict_no_space.txt')
  print(tokenizer.word_seg(text))

main()