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
  text1 = '''烏克蘭表示，烏軍正擴大在烏東閃電反攻俄羅斯行動。烏東盧甘斯克分離主義人士今天坦言，烏軍已進逼分離勢力占領區邊界。但美國總統拜登說，戰爭看來仍有一段長路。
路透社報導，俄羅斯軍隊本月遭逢重大挫敗，在烏克蘭東北部的哈爾科夫州（Kharkiv），烏軍在特種部隊帶頭下以裝甲部隊快速推進，迫使俄軍棄甲曳兵撤退。

烏克蘭總統澤倫斯基（Volodymyr Zelenskyy）昨天晚間發表談話時指出，烏軍本月至今已經收復約8000平方公里領土，接近地中海島國賽普勒斯（Cyprus）本島面積。

路透社尚無法確認烏克蘭宣稱奪回的領土全部規模。

澤倫斯基還表示，在這片已收復領土的約一半地區，已經完成他所謂的「穩定措施」，也就是完全保護安全及排除任何親俄分子。他並重申冀望動用軍隊奪回所有國土。

澤倫斯基的顧問阿列斯托維奇（Oleksiy Arestovych）今天表示，烏克蘭部隊正在攻擊俄軍占領的頓內茨克州（Donetsk）城鎮利曼（Lyman），並且等待機會在受俄羅斯控制的鄰州盧甘斯克州（Luhansk）收復領土。'''

  text = "聯合國教科文組織的簡稱是UNESCO，旨在通過教育、科學及文化來促進各國合作，對和平與安全作出貢獻。"
  tokenizer = SEG('dict_no_space.txt')
  print(tokenizer.word_seg(text1))

main()