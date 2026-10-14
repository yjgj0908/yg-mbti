import streamlit as st

st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기!",
    page_icon="⚡",
    layout="centered",
)

IMAGE_URL = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
    "sprites/pokemon/other/official-artwork/{}.png"
)

POKEMON = {
    "INTJ": {
        "ko": "뮤츠", "en": "Mewtwo", "id": 150,
        "type": "에스퍼",
        "feature": "뛰어난 지능과 강력한 초능력을 지닌 전설의 포켓몬",
        "reasons": [
            "깊이 생각하고 복잡한 문제의 해결책을 찾는 모습이 뮤츠와 닮았어.",
            "뚜렷한 목표를 세우고 자신만의 방식으로 계획을 세우는 전략가!",
        ],
    },
    "INTP": {
        "ko": "메타그로스", "en": "Metagross", "id": 376,
        "type": "강철 / 에스퍼",
        "feature": "네 개의 뇌가 컴퓨터처럼 작동한다고 알려진 포켓몬",
        "reasons": [
            "원리를 분석하고 논리적으로 생각하는 탐구적인 성격이 잘 어울려.",
            "호기심이 생기면 끝까지 파고들며 새로운 가능성을 찾아내는 타입!",
        ],
    },
    "ENTJ": {
        "ko": "리자몽", "en": "Charizard", "id": 6,
        "type": "불꽃 / 비행",
        "feature": "강력한 불꽃을 뿜으며 하늘을 나는 포켓몬",
        "reasons": [
            "목표를 향해 자신 있게 나아가는 추진력이 리자몽을 떠올리게 해.",
            "어려운 도전 앞에서도 해결 방법을 찾고 팀을 이끄는 리더형!",
        ],
    },
    "ENTP": {
        "ko": "피카츄", "en": "Pikachu", "id": 25,
        "type": "전기",
        "feature": "볼의 전기 주머니에 전기를 모으는 인기 포켓몬",
        "reasons": [
            "재치 있는 아이디어와 활발한 에너지로 주변을 깜짝 놀라게 해!",
            "새로운 시도를 즐기고 상황에 맞춰 유연하게 행동하는 점이 닮았어.",
        ],
    },
    "INFJ": {
        "ko": "가디안", "en": "Gardevoir", "id": 282,
        "type": "에스퍼 / 페어리",
        "feature": "소중한 트레이너를 지키려는 마음이 강한 포켓몬",
        "reasons": [
            "다른 사람의 마음을 세심하게 살피고 공감하려는 모습이 닮았어.",
            "눈앞의 일뿐 아니라 그 안에 담긴 의미와 미래까지 생각하는 유형!",
        ],
    },
    "INFP": {
        "ko": "이브이", "en": "Eevee", "id": 133,
        "type": "노말",
        "feature": "여러 가지 진화 가능성을 지닌 포켓몬",
        "reasons": [
            "자신만의 가치와 감성을 소중하게 여기며 다양한 가능성을 품고 있어.",
            "이브이처럼 자신에게 맞는 길을 천천히 찾아가는 모습이 잘 어울려!",
        ],
    },
    "ENFJ": {
        "ko": "푸린", "en": "Jigglypuff", "id": 39,
        "type": "노말 / 페어리",
        "feature": "노래로 상대를 잠들게 하는 둥글고 사랑스러운 포켓몬",
        "reasons": [
            "사람들과 어울리고 주변에 따뜻한 에너지를 전하는 모습이 닮았어.",
            "친구들의 장점을 발견하고 함께 성장하도록 응원하는 타입!",
        ],
    },
    "ENFP": {
        "ko": "파치리스", "en": "Pachirisu", "id": 417,
        "type": "전기",
        "feature": "전기를 모으는 볼과 꼬리를 지닌 포켓몬",
        "reasons": [
            "호기심이 많고 새로운 경험을 즐기는 밝은 성격이 잘 어울려.",
            "파치리스처럼 활기찬 에너지로 주변 분위기를 환하게 만들어!",
        ],
    },
    "ISTJ": {
        "ko": "거북왕", "en": "Blastoise", "id": 9,
        "type": "물",
        "feature": "등의 대포에서 강력한 물줄기를 발사하는 포켓몬",
        "reasons": [
            "맡은 일을 꼼꼼하게 확인하고 책임감 있게 해내는 모습이 닮았어.",
            "경험과 원칙을 바탕으로 차근차근 문제를 해결하는 든든한 타입!",
        ],
    },
    "ISFJ": {
        "ko": "해피너스", "en": "Blissey", "id": 242,
        "type": "노말",
        "feature": "상처 입은 포켓몬을 돌보는 다정한 포켓몬",
        "reasons": [
            "주변 사람의 필요를 알아차리고 조용히 도와주는 모습이 닮았어.",
            "작은 약속도 소중히 여기며 꾸준히 배려를 실천하는 유형!",
        ],
    },
    "ESTJ": {
        "ko": "괴력몬", "en": "Machamp", "id": 68,
        "type": "격투",
        "feature": "네 개의 팔로 강력한 기술을 사용하는 포켓몬",
        "reasons": [
            "목표와 역할을 분명히 정하고 실제 행동으로 옮기는 추진력이 있어.",
            "괴력몬처럼 책임감을 가지고 팀의 목표를 이루려는 모습이 닮았어!",
        ],
    },
    "ESFJ": {
        "ko": "토게피", "en": "Togepi", "id": 175,
        "type": "페어리",
        "feature": "행복한 기운을 나누는 알 모양의 포켓몬",
        "reasons": [
            "사람들과 조화를 이루고 서로 돕는 일을 중요하게 생각해.",
            "토게피처럼 다정하고 밝은 분위기로 주변에 기쁨을 전하는 타입!",
        ],
    },
    "ISTP": {
        "ko": "루카리오", "en": "Lucario", "id": 448,
        "type": "격투 / 강철",
        "feature": "파동을 감지하고 다루는 능력을 지닌 포켓몬",
        "reasons": [
            "문제가 생기면 상황을 관찰하고 원인을 분석하는 침착함이 닮았어.",
            "필요한 순간에 직접 해결책을 실행하는 실전형 문제 해결사!",
        ],
    },
    "ISFP": {
        "ko": "치코리타", "en": "Chikorita", "id": 152,
        "type": "풀",
        "feature": "머리의 잎으로 주변의 따뜻함과 습도를 감지하는 포켓몬",
        "reasons": [
            "자신만의 취향과 감각을 소중히 여기고 주변을 섬세하게 살펴.",
            "치코리타처럼 부드럽고 편안한 분위기를 만드는 모습이 닮았어!",
        ],
    },
    "ESTP": {
        "ko": "개굴닌자", "en": "Greninja", "id": 658,
        "type": "물 / 악",
        "feature": "민첩한 움직임으로 상대를 교란하는 포켓몬",
        "reasons": [
            "상황을 빠르게 파악하고 망설이기보다 직접 행동하는 편이야.",
            "개굴닌자처럼 변화에 유연하게 대응하고 새로운 도전을 즐겨!",
        ],
    },
    "ESFP": {
        "ko": "꼬부기", "en": "Squirtle", "id": 7,
        "type": "물",
        "feature": "물줄기를 뿜고 단단한 등껍질로 몸을 보호하는 포켓몬",
        "reasons": [
            "친구들과 함께하는 즐거운 순간과 새로운 경험을 좋아하는 유형!",
            "꼬부기처럼 장난기 있고 유쾌한 에너지로 주변을 즐겁게 해.",
        ],
    },
}

MBTI_TYPES = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ",
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600;700;900&display=swap');

.stApp {
    background: linear-gradient(
        180deg, #a8e5ff 0%, #e6f9ff 54%, #dff5cf 100%
    );
    color: #244566;
}
html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}
h1, h2, h3 {
    font-family: 'Jua', sans-serif !important;
    color: #244d72 !important;
}
.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    text-align: center;
    padding: 1.3rem 1rem 1.5rem;
    border: 4px solid white;
    border-radius: 30px;
    background: rgba(255,255,255,.78);
    box-shadow: 0 10px 0 rgba(66,126,145,.12);
    margin-bottom: 1.2rem;
}
.hero-tag {
    display: inline-block;
    padding: .4rem .9rem;
    border-radius: 999px;
    background: #e3f8d9;
    color: #39774b;
    font-weight: 900;
}
.hero-title {
    font-family: 'Jua', sans-serif;
    font-size: clamp(2.2rem, 6vw, 3.5rem);
    line-height: 1.25;
    margin: .8rem 0 .5rem;
    color: #244d72;
}
.hero-sub {
    font-size: 1.08rem;
    line-height: 1.8;
    color: #496d83;
    margin: 0;
}
div.stButton > button {
    width: 100%;
    min-height: 3.1rem;
    border: 2px solid #d1e8f5;
    border-radius: 15px;
    background: rgba(255,255,255,.94);
    color: #315c7d;
    font-size: 1.05rem;
    font-weight: 900;
    transition: all .18s ease;
}
div.stButton > button:hover {
    border-color: #55b8df;
    background: #e4f8ff;
    color: #214f75;
    transform: translateY(-2px);
}
.pill {
    display: inline-block;
    background: #e5f8db;
    color: #39764b;
    padding: .45rem 1rem;
    border-radius: 999px;
    font-weight: 900;
    margin-bottom: .7rem;
}
.pokemon-title {
    font-family: 'Jua', sans-serif;
    color: #28577e;
    font-size: clamp(2rem, 6vw, 3rem);
    margin: .2rem 0;
}
.english-name {
    color: #71899a;
    font-size: 1.15rem;
    font-weight: 700;
}
.type-pill {
    display: inline-block;
    background: #edf5ff;
    border: 1px solid #d6e7f7;
    border-radius: 999px;
    padding: .35rem .9rem;
    margin: .7rem 0;
    color: #315c7d;
    font-weight: 800;
}
.info-box {
    text-align: left;
    background: #f3faff;
    border-radius: 18px;
    padding: 1rem 1.2rem;
    margin-top: 1rem;
    line-height: 1.85;
    color: #36546b;
}
.info-box b {
    color: #2c7195;
    font-size: 1.08rem;
}
.footer-note {
    text-align: center;
    color: #52778a;
    font-size: .85rem;
    line-height: 1.7;
    margin-top: 1.5rem;
}
@media (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .hero {
        padding: 1rem .7rem;
    }
    .hero-sub {
        font-size: .98rem;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="hero-tag">🌿 POKÉMON BEST FRIEND TEST</div>
  <div class="hero-title">⚡ MBTI 단짝 포켓몬 찾기!</div>
  <p class="hero-sub">
    내 성격과 찰떡인 포켓몬은 누구일까?<br>
    MBTI를 고르고 나만의 단짝 포켓몬을 만나 봐!
  </p>
</div>
""", unsafe_allow_html=True)

if "chosen_mbti" not in st.session_state:
    st.session_state.chosen_mbti = None

if "celebrate_for" not in st.session_state:
    st.session_state.celebrate_for = None

st.markdown("## 🔎 먼저 나의 MBTI를 골라 줘!")
st.caption("아래 16가지 버튼 중 하나를 눌러 봐!")

for start in range(0, len(MBTI_TYPES), 4):
    columns = st.columns(4, gap="small")

    for column, mbti in zip(
        columns, MBTI_TYPES[start:start + 4]
    ):
        with column:
            if st.button(
                mbti,
                key=f"mbti_{mbti}",
                use_container_width=True,
            ):
                st.session_state.chosen_mbti = mbti
                st.session_state.celebrate_for = mbti

chosen = st.session_state.chosen_mbti

if chosen:
    data = POKEMON[chosen]

    if st.session_state.celebrate_for == chosen:
        st.balloons()
        st.snow()
        st.toast("단짝 포켓몬을 찾았어!", icon="🎊")
        st.session_state.celebrate_for = None

    st.markdown("---")

    st.markdown(
        f'<div style="text-align:center;margin:1rem 0 .7rem;">'
        f'<span class="pill">🎉 {chosen} 단짝 포켓몬 발견!</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([1, 1.15], gap="large")

    with left:
        st.image(
            IMAGE_URL.format(data["id"]),
            caption=f'{data["ko"]} ({data["en"]})',
            use_container_width=True,
        )

    with right:
        st.markdown(
            f'<div style="padding:.4rem 0 .8rem;">'
            f'<div class="pokemon-title">{data["ko"]}</div>'
            f'<div class="english-name">{data["en"]}</div>'
            f'<div class="type-pill">⚔️ 타입: {data["type"]}</div>'
            f'<div class="info-box">'
            f'<b>✨ 포켓몬 특징</b><br>{data["feature"]}'
            f'</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="info-box">'
        '<b>💚 너와 어울리는 이유</b></div>',
        unsafe_allow_html=True,
    )

    for reason in data["reasons"]:
        st.markdown(f"- {reason}")

    st.success(
        f'축하해! 너의 MBTI 단짝은 '
        f'**{data["ko"]} ({data["en"]})** 이야! 🎊'
    )

    if st.button(
        "🔄 다시 고르기",
        key="reset",
        use_container_width=True,
    ):
        st.session_state.chosen_mbti = None
        st.session_state.celebrate_for = None
        st.rerun()

st.markdown("""
<div class="footer-note">
  🌈 MBTI와 포켓몬의 연결은 공식 설정이 아닌 재미를 위한 창작 해석이야.<br>
  포켓몬 이미지와 웹폰트는 외부에서 불러오므로 인터넷 연결이 필요해.
</div>
""", unsafe_allow_html=True)
