import streamlit as st

st.title("😀인공지능(Artificial Intelligence)")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3 = st.tabs(['인공지능 역사','머신러닝', '딥러닝'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.subheader('1. 간단한 자기소개')
    st.markdown("이름은 **박찬웅**, 2024년 기준으로 나이는 19세 **고3**이며 **수능**을 앞두고 있는 **수험생**이다.")

    st.subheader('2. 나의 역사')
    st.markdown('하늘보리 어린이집, 강남 유치원, 갈곡초등학교, 대구옥포초등학교, 달성중학교, 그리고 현재 화원고등학교까지 많은 학교를 거쳐 현재 고등학교 3학년이 되었다.')
    st.markdown(':red[[**밑에 사진들은 나의 모교들**]]')
    st.image('https://yongin.grandculture.net/Image?localName=yongin&id=GC009P0182&t=middle')

    st.caption('출처: 내 머릿속')

