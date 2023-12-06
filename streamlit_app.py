from pathlib import Path
import re
import gzip, json
from textblob import TextBlob
import pandas as pd
import pronouncing
import nltk
nltk.download('all')
from io import StringIO

#-------------------------------------------------------------------------------------

import streamlit as st

st.header("영시 분석 결과 보기")

st.write('download corpus: http://static.decontextualize.com/gutenberg-poetry-v001.ndjson.gz')

uploaded_file = st.file_uploader("Upload text files", accept_multiple_files=True)
uploaded_file_2 = st.file_uploader("Upload corpus")

#--------------------------------------------------------------------------------------

book_num = st.text_input("input book numbers from corpus divided by ':'", key = '1')
book_nums = book_num.split(':')

#--------------------------------------------------------------------------------------

all_text = []


def get():
    if uploaded_file is not None and uploaded_file_2 is not None:
        for i in range(0, len(uploaded_file)):
            stringio = StringIO(uploaded_file[i].getvalue().decode("utf-8"))
            string_data = stringio.read()
            trimmed_poems =  re.sub("[\n0-9]", "", string_data)
            text = trimmed_poems.split(',')
            all_text.extend([text])

        all_lines = []
        for line in gzip.open(uploaded_file_2):
            all_lines.append(json.loads(line.strip()))
        a = len(all_lines)
        text = []
        for i in range(0,a):
            each_line =  all_lines[i]
            dict_items = each_line.items()

            for b in range(0, len(book_nums)):
                if list(dict_items)[1] ==  ('gid', book_nums[b]):
                    text.append(each_line.get('s'))
        all_text.extend(text)
        return all_text

    elif uploaded_file is not None and uploaded_file_2 is None:
        for i in range(0, len(uploaded_file)):
            stringio = StringIO(uploaded_file[i].getvalue().decode("utf-8"))
            string_data = stringio.read()
            trimmed_poems =  re.sub("[\n0-9]", "", string_data)
            text = trimmed_poems.split(',')
            all_text.extend([text])
        return all_text

    elif uploaded_file_2 is not None and uploaded_file is None:
        all_lines = []
        for line in gzip.open(uploaded_file_2):
            all_lines.append(json.loads(line.strip()))
        a = len(all_lines)
        text = []
        for i in range(0,a):
            each_line =  all_lines[i]
            dict_items = each_line.items()

            for b in range(0, len(book_nums)):
                if list(dict_items)[1] ==  ('gid', book_nums[b]):
                    text.append(each_line.get('s'))
        all_text.extend(text)
        return all_text
    
    else:
        st.markdown("no files uploaded")


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

get_from = st.button('see results', key = 11)

if get_from == True:
    all_text = get()
    result(all_text)


reset_button = st.button('reset', key = 12)

if reset_button == True:
    all_text = []
