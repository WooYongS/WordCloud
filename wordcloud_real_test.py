import time
from PIL import Image
# from konlpy.tag import Okt

from pprint import pprint
import numpy as np
import urllib.parse
import xml.sax.saxutils as saxutils

import os
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

# print('나오는 거 맞아?')/

f = open("./0722_WD.txt", 'r')

# f = open("./0530_WD.txt", 'r', encoding='utf-8')

stringdata = f.read()

print(stringdata)

# stringdata = sys.argv[1]

# stringdata = """1캥거루 2토끼 3강아지 4고양이 5코알라 6고릴라 7원숭이 8고래 9낙타 10뱀
# 11물개 12쥐 13소 14말 15돼지 16거북이 17악어 18호랑이 19표범 20치타
# 21늑대 22여우 23스컹크 24두더지 25돌고래 26도마뱀 27독소리 28바다표범 29가재
# 30랍스타 31원앙 32까마귀 33오리 34앵무새 35부엉이 36참새 37꾀꼬리 38나비
# 39잠자리 40이구아나 41카멜레온 42개미핥기 43거미 44잉어 45곰 46펭귄 47거위
# 48박쥐 49병아리 50닭 51멧돼지 52갈매기 53코뿔소 54사슴 55코끼리 56하마"""

	
def draw_wordcloud(text):

	## 특정 단어 없애기
	
	text = text.replace('\n','')
	text = text.replace('\t','')

	text = text.replace('강의','')
	text = text.replace('교육','')
	text = text.replace('신임','')
	text = text.replace('강사','')
	text = text.replace('부점','')
	text = text.replace('회의','')
	text = text.replace('보고','')
	

    # 인사성과
	text = text.replace('지점장','')
	text = text.replace('올해','')
	text = text.replace('직원','')
	text = text.replace('인사','')
	text = text.replace('반영','')
	text = text.replace('공지','')

	#경영현안/전략
	text = text.replace('수행','')
	text = text.replace('원스','')
	text = text.replace('전반','')
	text = text.replace('부탁','')
	text = text.replace('직원','')
	text = text.replace('분모','')
	text = text.replace('연금','')
	text = text.replace('부관리우수','')

	#리더십
	text = text.replace('드림','')
	text = text.replace('설정','')
	text = text.replace('무엇','')
	text = text.replace('직원','')
	text = text.replace('부분','')
	text = text.replace('점장','')
	text = text.replace('최근','')
	text = text.replace('영업','')
	text = text.replace('포장','')
	text = text.replace('자임','')
	text = text.replace('일부','')

	#플랫폼
	text = text.replace('배달','')
	text = text.replace('요기','')
	text = text.replace('플랫폼','')
	text = text.replace('기업','')
	text = text.replace('행사시','')
	text = text.replace('여부','')
	text = text.replace('은행','')
	text = text.replace('벅스','')
	text = text.replace('스타','')

	#칭찬
	text = text.replace('대리','')
	text = text.replace('지점','')	
	text = text.replace('모습','')
	text = text.replace('팀장','')	
	text = text.replace('계장','')
	text = text.replace('차장','')	
	text = text.replace('과','')
	text = text.replace('종합','')	
	text = text.replace('부서','')
	text = text.replace('텐데','')

	text = text.replace('퇴근','')
	text = text.replace('생각','')
	text = text.replace('신경','')
	text = text.replace('생활','')
	text = text.replace('행동','')
	text = text.replace('생각','')
	text = text.replace('하나','')
	text = text.replace('우리','')
	text = text.replace('사용','')
	text = text.replace('이용','')

	text = text.replace('이용','')
	text = text.replace('이용','')
	text = text.replace('이용','')
	
	text = text.replace('연수','')
	text = text.replace('상무','')
	text = text.replace('승격','')
	text = text.replace('고생','')

	text = text.replace('준비','')
	text = text.replace('시간','')
	
	text = text.replace('영상','')
	text = text.replace('오늘','')
	text = text.replace('그룹','')
	text = text.replace('입장','')
	text = text.replace('하루하루','')
	text = text.replace('활용','')

		
	text = text.replace('필요','')
	text = text.replace('부족','')
	text = text.replace('이상','')
	text = text.replace('시장','')
	text = text.replace('지금','')
	text = text.replace('미래','')
	

	##### 한국어사전 기준의 명사들만 리스트로 만들기 #####
	engine = Mecab()
	nouns = engine.nouns(text)
	nouns = [n for n in nouns if len(n) > 1]

	#### 전달받은 문자열을 띄어쓰기 기준으로 명사 리스트 생성 ####
	# nouns = text.split()
	# nouns = text

	print("----print(nouns)----")
	print(nouns)
		
    #### 빈도수를 계산 #####
	count = Counter(nouns)
		
	######## 몇개의 단어 추출할 건지 설정 ##########
	tags = count.most_common(87)
	######## 몇개의 단어 추출할 건지 설정 ##########
	
	print("----print(count.most_common(100)) 단어별 빈도수 리스트 생성----")
	print(tags)
	
	#WordCloud, matplotlib: 단어 구름 그리기
	font_path = 'KBFGTextM.ttf'
	wc = WordCloud(font_path=font_path,background_color='white',width=800, height=600)
	
	# wc = WordCloud(min_font_size=35,max_font_size=50,font_path=font_path,background_color='white', width=800, height=600)
	
	# 빈도수로 워드클라우드 생성
	cloud = wc.generate_from_frequencies(dict(tags))
	# cloud = wc.generate(tags)

	## color customizing
	# cloud = cloud.recolor(color_func=make_colors,random_state=True)
	
	# cloud = wc.generate(text)
	plt.figure(figsize=(10,8))
	plt.axis('off')
	plt.imshow(cloud, interpolation='lanczos')
	#plt.savefig('wordcloud.png')
	
	######### 생성될 이미지 파일명 #########
	plt.savefig("./0722_3.png")
	######### 생성될 이미지 파일명 #########
	
	plt.close('all')
	
# cloud_mask = np.array(Image.open("cloudmask2.png"))

draw_wordcloud(stringdata)

