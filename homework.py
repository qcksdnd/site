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


with tab2:
    # tab B를 누르면 표시될 내용
    st.write("")
    st.subheader('1.인공지능&머신러닝&딥러닝')
    st.image("images/ai_structure.jpg")
    st.caption("▲인공지능, 머신러닝, 딥러닝의 관계도")

    st.subheader("2. 머신러닝(Machine Learning)")
    st.markdown('머신러닝은 인공지능을 구현하는 대표적인 방법 중의 하나로, **데이터에서 패턴을 찾아내 문제애 대한 답을 예측하는 알고리즘**이다. '
                '머신러닝의 활용 분야로 금융, 이미지프로세싱, 금융분석 및 탐지 분야, 음성인식, 로봇제어 분야 등이 있다.')
    st.write("")
    st.markdown("머신러닝의 학습 방법에는 지도 학습, 비지도 학습, 강화 학습의 3가지로 나뉠 수 있다.")
    st.write("")
    st.markdown("""
    - 지도 학습
    - 비지도 학습
    - 강화 학습
    """)
    st.markdown(":red[**① 지도 학습(Supervised Learning**)] : 지도 학습은 **데이터와 정답**을 함께 제시하여 학습하는 방법이다. "
                "예를 들어, 고양이와 개를 학습시킨다고 했을 때 고양이 데이터와 개 사진 데이터를 입력으로 넣어주면서 정답(고양이, 개) 레이블을 함께 주면서 학습시킨다."
                "지도 학습에는 크게 분류와 회귀 모델로 나뉠 수 있다.")
    st.video("https://youtu.be/hnc1DGz9UCU")
    st.markdown(":red[**② 비지도 학습(Unsupervised Learning)**] : 비지도 학습은 정답이 없는 **데이터만** 주고 학습하게 방법이다. 정답이 없기 때문에 입력 데이터의 패턴이나 특성을 통해 학습하게 된다."
                "마찬가지로 고양이과 개를 학습시킬 때 고양이과 개 사진 데이터만 입력으로 주고 주어진 데이터를 바탕으로 고양이와 개의 특성을 찾아내는 방식이다."
                " 비지도 학습의 대표적인 모델로 군집화가 있다.")
    st.video("https://youtu.be/xwe1cbZaFEg")
    st.markdown(":red[**③ 강화 학습(Reinforcement Learning)**] : 강화 학습은 입력 데이터를 학습하여 **경험과 보상**을 통해 목표값을 찾도록 학습하는 방법이다. 즉 입-출려간의 상관관계를 찾는 것이 아니라, 시행착오에 대한 보상 체계를 바탕으로"
                "지속적인 경험에 통해 최선책을 찾도록 하는 방법이다. 주로 자율주행자동차나 게임, 주식 등에 활용된다.")
    st.video("https://youtu.be/BPCAP7DHLYw")

with tab3:
    # tab B를 누르면 표시될 내용
    st.write("")
    st.subheader('딥러닝(Deep Learning)')
    st.markdown("딥 러닝은 인간의 **신경망을 모방**하여 학습하게 하는 기계학습 방법이다. 인간의 뇌는 약 860억 개의 뉴런이 연결되어 신경망을 구성한다."
                " 이러한 신경망을 통해 다양한 감정을 느끼고 생각하게 되는 것이다. 이런 인간의 뇌 신경망을 모방한 것이 **인공 신경망**이다. "
                " 인공 신경망은 **퍼셉트론**(인간의 뉴런에 해당)을 기본 단위로 사용하며, 이 퍼셉트론이 여러 개 연결되어 **심층 인공 신경망(DNN)**을 구성한다."
                )
    st.video("https://youtu.be/kvAa-76IWHc")



