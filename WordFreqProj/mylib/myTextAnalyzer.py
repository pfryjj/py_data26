from matplotlib.font_manager import FontPath
import pandas as pd
from konlpy.tag import Okt
from collections import Counter

def load_corpus(datafile):
    return pd.read_csv(datafile)

def get_freq_word(data_df, target_col):
    # 분석 대상 컬럼을 리스트로 출력
    target_list = list(data_df[target_col].dropna())

    # 리스트의 문서 -> 단어 리스트 생성 (품사태깅, 불용어 제거)
    word_list = get_korean_word_list(target_list)

    # 단어 리스트로부터 Counter 객체 생성
    counter = Counter(word_list)
    return counter

def get_korean_word_list(review_list):
    tagger = Okt().pos
    my_tags = ['Noun', 'Adjective', 'Verb']
    my_stopwords = ['영화', '것', '이', '더']

    result_list = []
    for review in review_list:
        word_list = [word for word, tag in tagger(str(review)) if word not in my_stopwords and tag in my_tags]
        result_list.extend(word_list)

    return result_list

def generate_wordcloud(counter, num_words):
    from wordcloud import WordCloud
    font_path = 'C:/Windows/Fonts/malgun.ttf'
    wc = WordCloud(
        background_color = 'ivory',
        width = 800,
        height = 600,
        max_words= num_words,
        font_path= font_path
    )
    return wc.generate_from_frequencies(counter)