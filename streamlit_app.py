from pathlib import Path
import re
import gzip, json
from textblob import TextBlob
import pandas as pd
import pronouncing
import nltk
import os


#-------------------------------------------------------------------------------------

import streamlit as st

st.header("영시 분석 결과 보기")

st.write('download corpus: http://static.decontextualize.com/gutenberg-poetry-v001.ndjson.gz')
path = st.text_input('input file path of the folder where you saved the corpus and text files, and press enter')
cwd = os.getcwd()

st.write(cwd)


col1, col2 = st.columns(2)

all_text = []

#--------------------------------------------------------------------------------------

def get_text(A):
    all_lines = []

    file_path = Path(A + '/' + book_num2 + '.txt')
    file_path_2 = os.path.join(cwd, file_path)

    f = open(file_path_2, encoding='UTF8')
    lines = f.readlines()

    for line in lines:
        all_lines.append(line)

    f.close()

    trimmed_poems =  re.sub("[\n0-9]", "", str(all_lines))
    text = trimmed_poems.split(',')
    all_text.extend([text])

    return all_text

#--------------------------------------------------------------------------------------

def get_corpus(B):
    all_lines = []

    file_path = Path(B + '/gutenberg-poetry-v001.ndjson.gz')
    file_path_2 = os.path.join(cwd, file_path)

    for line in gzip.open(file_path_2):
        all_lines.append(json.loads(line.strip()))
        
    a = len(all_lines)
    text = []
    for i in range(0,a):
        each_line =  all_lines[i]
        dict_items = each_line.items()
        if list(dict_items)[1] ==  ('gid', book_num):
            text.append(each_line.get('s'))

    all_text.extend(text)

    return all_text


#--------------------------------------------------------------------------------------

def result(C):
    lower_text = str(C).lower()
    no_punc_lower_text = re.sub('[\{\}\/?.,;:|\)*~`!^\-_+<>@\#$%&\\=\(\'\"]', ' ', lower_text)
    text_analysis = TextBlob(no_punc_lower_text)

    words_num = len(text_analysis.words)

    sent = text_analysis.sentiment

    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    word_tokens = text_analysis.words
    trimmed_text = []
    for w in word_tokens:
        if w not in stop_words:
            trimmed_text.append(w)
    trimmed_text_analysis = TextBlob(str(trimmed_text))
    # wordcount = trimmed_text_analysis.word_counts
    trimmed_word_tokens = trimmed_text_analysis.words

    c = dict(text_analysis.tags)
    d = c.values()
    text_pos = list(d)
    adjv = ((text_pos.count('JJ') + text_pos.count('JJR') + text_pos.count('JJS') + text_pos.count('RB') + text_pos.count('RBR') + text_pos.count('RBS'))/words_num)*100

    may_count = text_analysis.word_counts['may']
    might_count = text_analysis.word_counts['might']
    can_count = text_analysis.word_counts['can']
    could_count = text_analysis.word_counts['could']
    would_count = text_analysis.word_counts['would']
    should_count = text_analysis.word_counts['should']
    will_count = text_analysis.word_counts['will']
    must_count = text_analysis.word_counts['must']

    modal_1 = ((may_count + might_count)/words_num)*100
    modal_2 = ((can_count + could_count)/words_num)*100
    modal_3 = ((would_count + should_count)/words_num)*100
    modal_4 = (will_count/words_num)*100
    modal_5 = (must_count/words_num)*100

    wh_word = ((text_pos.count('WDT') + text_pos.count('WP') + text_pos.count('WP$') + text_pos.count('WRB'))/words_num)*100

    not_count = text_analysis.word_counts['not']
    nt_count = text_analysis.word_counts["n't"]
    none_count = text_analysis.word_counts['none']
    nothing_count = text_analysis.word_counts['nothing']
    nobody_count = text_analysis.word_counts['nobody']
    nowhere_count = text_analysis.word_counts['nowhere']
    nor_count = text_analysis.word_counts['nor']
    neither_count = text_analysis.word_counts['neither']

    neg_word = ((not_count + nt_count + none_count + nothing_count + nobody_count + nowhere_count + nor_count + neither_count)/words_num)*100


    from collections import defaultdict
    by_rhyming_part = defaultdict(lambda: defaultdict(list))

    for i in range(0, len(trimmed_word_tokens)):
        match = re.search(r'(\b\w+\b)\W*$', trimmed_word_tokens[i])
        if match:
            last_word = match.group()
            pronunciations = pronouncing.phones_for_word(last_word)
            if len(pronunciations) > 0:
                rhyming_part = pronouncing.rhyming_part(pronunciations[0])
                by_rhyming_part[rhyming_part][last_word.lower()].append(trimmed_word_tokens[i])

    rhyme_groups = [group for group in by_rhyming_part.values() if len(group) >= 4]

    rhyme = (len(rhyme_groups) / words_num)*100

    df = pd.DataFrame([
            {"분석요소": "감정(polarity)", "result" : sent[0]},
            {"분석요소": "감정(subjectivity)", "result" : sent[1]},
            {"분석요소": "형용사/부사", "result": adjv},
            {"분석요소": "조동사(약한)", "result": modal_1},
            {"분석요소": "조동사(조금 약한)", "result": modal_2},
            {"분석요소": "조동사(중간)", "result": modal_3},
            {"분석요소": "조동사(조금 강한)", "result": modal_4},
            {"분석요소": "조동사(강한)", "result": modal_5},
            {"분석요소": "WH-word", "result": wh_word},
            {"분석요소": "negative word", "result": neg_word},
            {"분석요소": "rhyme groups", "result": rhyme},
            ])
    st.data_editor(df)


#--------------------------------------------------------------------------------------


with col1:
    st.markdown("get from corpus")
    book_num = st.text_input('input book number and press get button', key = '1')
    get_from_corpus = st.button('get', key = 11)

    if get_from_corpus == True:
        all_text = get_corpus(path)
        result(all_text)
  
# ----------------------------------------------------------------------------------------------

with col2:
    st.markdown("get from text file")    
    book_num2 = st.text_input('input file name and press get button', key ='2')
    get_from_text = st.button('get', key = 12)
            
    if get_from_text == True:
        all_text = get_text(path)
        result(all_text)
