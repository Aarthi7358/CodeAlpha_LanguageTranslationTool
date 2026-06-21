import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Anime AI Translator",
    page_icon="🌸",
    layout="centered"
)

st.markdown("""
<style>

/* Animated Background */
.stApp{
    background: linear-gradient(-45deg,#0f0c29,#302b63,#24243e,#6a11cb);
    background-size:400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* Floating Sparkles */
.sparkle{
    position:fixed;
    color:white;
    animation: float 8s linear infinite;
    opacity:0.6;
    z-index:0;
}

@keyframes float{
    0%{
        transform:translateY(100vh) rotate(0deg);
    }
    100%{
        transform:translateY(-100px) rotate(360deg);
    }
}

/* Glass Card */
.main-card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    border-radius:25px;
    padding:25px;
    border:1px solid rgba(255,255,255,0.2);
    box-shadow:0 0 30px rgba(255,255,255,0.1);
}

/* Title Glow */
.title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:white;
    text-shadow:
        0 0 10px #ff00ff,
        0 0 20px #ff00ff,
        0 0 40px #8a2be2;
    animation:pulse 2s infinite;
}

@keyframes pulse{
    50%{
        transform:scale(1.03);
    }
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:#dddddd;
    margin-bottom:20px;
}

/* Buttons */
.stButton>button{
    width:100%;
    height:55px;
    border-radius:15px;
    border:none;
    font-size:18px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    transform:scale(1.05);
}

/* Text Area */
textarea{
    border-radius:15px !important;
}

/* Hide Streamlit Footer */
footer{
    visibility:hidden;
}
</style>

<div class="sparkle" style="left:10%;font-size:25px;">✨</div>
<div class="sparkle" style="left:25%;font-size:20px;animation-delay:2s;">⭐</div>
<div class="sparkle" style="left:40%;font-size:30px;animation-delay:4s;">✨</div>
<div class="sparkle" style="left:65%;font-size:22px;animation-delay:1s;">⭐</div>
<div class="sparkle" style="left:85%;font-size:28px;animation-delay:3s;">✨</div>

<div class="title">🌸 Anime AI Translator 🌸</div>
<div class="subtitle">
Translate languages with futuristic AI magic ✨
</div>

""", unsafe_allow_html=True)

languages = {
    "English":"en",
    "Tamil":"ta",
    "Hindi":"hi",
    "French":"fr",
    "German":"de",
    "Spanish":"es",
    "Japanese":"ja",
    "Korean":"ko",
    "Chinese":"zh-CN"
}

st.markdown('<div class="main-card">', unsafe_allow_html=True)

col1,col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "🌍 Source Language",
        list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "🎯 Target Language",
        list(languages.keys())
    )

text = st.text_area(
    "✍ Enter Text",
    height=180,
    placeholder="Type your message here..."
)

if st.button("✨ Translate Now ✨"):

    if text.strip():

        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("Translation Successful 💜")

            st.text_area(
                "🌸 Translated Text",
                translated,
                height=180
            )

            st.code(translated)

        except Exception as e:
            st.error(str(e))

    else:
        st.warning("Enter some text first!")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <center>
    <br>
    <h4 style='color:white;'>
    🤖 Powered by AI | Made for CodeAlpha Internship
    </h4>
    </center>
    """,
    unsafe_allow_html=True
)