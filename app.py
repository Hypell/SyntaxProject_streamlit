import streamlit as st
import pandas as pd

# 제목
st.subheader('사조별 영국 시 양상 분석 연구 결과')

# 사이드바
st.sidebar.caption('choose an age')
age1 = st.sidebar.checkbox('Renaissance')
age2 = st.sidebar.checkbox('17th century')
age3 = st.sidebar.checkbox('Romanticism')
age4 = st.sidebar.checkbox('Victorian')
age5 = st.sidebar.checkbox('Contemporary')

if age1:
    st.sidebar.caption("choose a poet from Renaissance")
    poet1_1 = st.sidebar.checkbox('크리스토퍼 말로')
    poet1_2 = st.sidebar.checkbox('에드먼드 스펜서')
    poet1_3 = st.sidebar.checkbox('윌리엄 셰익스피어')

if age2:
    st.sidebar.caption("choose a poet from 17th century")
    poet2_1 = st.sidebar.checkbox('존 던')
    poet2_2 = st.sidebar.checkbox('앤드루 마벌')
    poet2_3 = st.sidebar.checkbox('벤 존슨')

if age3:
    st.sidebar.caption("choose a poet from Romanticism")
    poet3_1 = st.sidebar.checkbox('윌리엄 워즈워스')
    poet3_2 = st.sidebar.checkbox('존 키츠')
    poet3_3 = st.sidebar.checkbox('퍼시 비시 셸리')

if age4:
    st.sidebar.caption("choose a poet from Victorian")
    poet4_1 = st.sidebar.checkbox('알프레드 테니슨')
    poet4_2 = st.sidebar.checkbox('로버트 브라우닝')
    poet4_3 = st.sidebar.checkbox('제라드 맨리 홉킨스')

if age5:
    st.sidebar.caption("choose a poet from Contemporary")
    poet5_1 = st.sidebar.checkbox('t.s. 엘리엇')
    poet5_2 = st.sidebar.checkbox('웰리엄 예이츠')



# 시인 별 데이터들










# 본 페이지

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["주제", "감정", "문장 형태", "형용사/부사", "조동사", 'WH-word', 'Negation', 'N-Gram', 'Rhyme'])

with tab1:
    st.markdown("단어로 주제 찾기")


with tab2:
    st.markdown("감정 분석하기")



with tab3:
    st.markdown("문장 형태별 사용 빈도 수")



with tab4:
    st.markdown("형용사/부사 사용 빈도 수")



with tab5:
    st.markdown("조동사 사용 빈도 수")



with tab6:
    st.markdown("WH-word 사용 빈도 수")



with tab7:
    st.markdown("Negation 사용 빈도 수")



with tab8:
    st.markdown("N-GRam")



with tab9:
    st.markdown("Rhyme")



