import streamlit as st

st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기!",
    page_icon="⚡",
    layout="centered",
)

# 포켓몬 공식 아트워크 이미지 주소
ARTWORK_URL = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
    "sprites/pokemon/other/official-artwork/{}.png"
)

# MBTI별 포켓몬 데이터
POKEMON = {
    "INTJ": {
        "ko": "뮤츠", "en": "Mewtwo", "id": 150,
        "type": "에스퍼",
        "features": "뛰어난 지능과 강력한 초능력을 지닌 전설의 포켓몬",
        "reasons": [
            "깊이 생각하고 복잡한 문제의 해결책을 찾는 모습이 뮤츠와 닮았어.",
            "뚜렷한 목표를 세우고 자신만의 방식으로 계획을 세우는 전략가!",
        ],
    },
    "INTP": {
        "ko": "메타그로스", "en": "Metag
