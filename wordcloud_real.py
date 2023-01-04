import time
# from PIL import Image
# from konlpy.tag import Okt

from pprint import pprint
import numpy as np
import urllib.parse
import xml.sax.saxutils as saxutils

import sys

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from eunjeon import Mecab
from collections import Counter

# import nltk

# okt = Okt()

# # # 하나의 문장을 토큰화 한 후 텍스트와 품사태깅을 / 구분자로 묶어준다.
# def tokenizing(docs):
    # return ['/'.join(t) for t in okt.pos(docs,norm=True, stem=True)]

# import nltk

# term_frequency()함수는 위에서 만든 selected_words의 갯수에 따라서 각 리뷰와 매칭하여 상위 텍스트가 
# 각 리뷰에 얼만큼 표현되는지 빈도를 만들기 위한 함수
# def term_frequency(doc):
    # return [doc.count(word) for word in selected_words]

		
# 20210310_조직문화
# 20210310_경영전략
# 20210310_성과관리
# 20210310_인사복지


## 워드클라우드 컬러 커스터마이징
# def make_colors(word,font_size,position,orientation,random_state,**kwargs):
	# color = "#d4b4f8"
	# return color

	

f = open("text.txt", 'r', encoding='euc-kr')
# stringdata = f.read()
stringdata = sys.argv[1]

	
def draw_wordcloud(text):

	## 특정 단어 없애기
	# text = text.replace('직원','')

	text = text.replace('\n','')
	text = text.replace('\t','')
	
	# engine = Mecab()
	# nouns = engine.nouns(text)
	# nouns = [n for n in nouns if len(n) > 1]

	nouns = text.split()

	######## 몇개의 단어 추출할 건지 설정 ##########
	count = Counter(nouns)
	tags = count.most_common(100)
	print(tags)
	######## 몇개의 단어 추출할 건지 설정 ##########
	
	# tags = tags.encode('utf8')

	#WordCloud, matplotlib: 단어 구름 그리기
	font_path = 'KBFGTextM.ttf'
	# wc = WordCloud(font_path=font_path,background_color='white',mask = cloud_mask,width=800, height=600)
	
	wc = WordCloud(max_font_size=30,min_font_size=30, font_path=font_path,background_color='white',width=1400, height=1000)
	
	# 빈도수로 워드클라우드 생성
	cloud = wc.generate_from_frequencies(dict(tags))
    # cloud = wc.generate(nouns)


	## color customizing
	# cloud = cloud.recolor(color_func=make_colors,random_state=True)
	

	plt.figure(figsize=(15,11))
	plt.axis('off')
	plt.imshow(cloud, interpolation='lanczos')
	#plt.savefig('wordcloud.png')
	
	######### 생성될 이미지 파일명 #########
	plt.savefig("./images/nation.png")
	######### 생성될 이미지 파일명 #########
	
	plt.close('all')
	
# cloud_mask = np.array(Image.open("cloudmask2.png"))

draw_wordcloud(stringdata)

print(sys.argv)






