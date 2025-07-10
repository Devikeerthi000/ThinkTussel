import streamlit as st
from debate.debate_manager import run_debate

st.set_page_config(page_title="ThinkTussel: LLM Debate Arena", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    html, body, .main, .block-container, [data-testid="stAppViewContainer"] {
        background-color: #eae6dd !important;
        font-family: Georgia, serif;
        color: #222;
    }

    .title {
        font-size: 64px;
        font-weight: 700;
        color: #1a1a1a;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 16px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #444;
        text-align: center;
        margin-top: 0px;
        margin-bottom: 45px;
    }

    .input-label {
        font-size: 22px;
        font-weight: bold;
        color: #111;
        margin-top: 30px;
        margin-bottom: 10px;
    }

    .stTextInput > div > div > input {
        border: 2px solid black !important;
        padding: 14px;
        border-radius: 6px;
        font-size: 16px;
        font-family: Georgia, serif;
    }

    .stSelectbox > div {
        font-size: 16px;
    }

    .stButton>button {
        background-color: black;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 26px;
        font-size: 18px;
        font-family: Georgia, serif;
        font-weight: bold;
        margin-top: 30px;
        transition: all 0.3s ease;
        outline: none !important;
        box-shadow: none !important;
    }

    .stButton>button:hover {
        background-color: #444;
        transform: scale(1.03);
        color: #fff;
    }

    .stButton>button:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    .role {
        font-weight: bold;
        font-size: 18px;
        margin-top: 35px;
        margin-bottom: 10px;
        color: #2a2a2a;
    }

    .message {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 18px;
        font-size: 16px;
        line-height: 1.6;
        color: #222;
        border: 1px solid #dcd9d2;
        box-shadow: 2px 2px 4px rgba(0,0,0,0.04);
    }

    .judgment {
        background-color: #f3f2ef;
        padding: 25px;
        border-left: 4px solid #333;
        border-radius: 8px;
        font-size: 16px;
        line-height: 1.6;
        color: #111;
        margin-top: 50px;
        margin-bottom: 60px;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Subtitle
st.markdown("<div class='title'>ThinkTussel</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Reason. Refute. Rethink.</div>", unsafe_allow_html=True)

# Input: Debate Topic
st.markdown("<div class='input-label'>Enter a Debate Topic:</div>", unsafe_allow_html=True)
topic = st.text_input(" ", label_visibility="collapsed")

# Input: Round Selection
round_labels = [f"Round {i}" for i in range(1, 6)]
st.markdown("<div class='input-label'>Select Number of Rounds:</div>", unsafe_allow_html=True)
round_choice = st.selectbox(" ", options=round_labels, index=1, label_visibility="collapsed")
rounds = int(round_choice.split(" ")[-1])  # Extract number from label

# Start Button & Logic
if st.button("Start Debate") and topic:
    with st.spinner("Let the debate begin..."):
        transcript, judgment = run_debate(topic, rounds)

    # Display Transcript
    st.markdown("<div class='subtitle'>Debate Transcript</div>", unsafe_allow_html=True)
    for idx, turn in enumerate(transcript, 1):
        st.markdown(f"<div class='role'>Turn {idx} - {turn['role']}:</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='message'>{turn['content']}</div>", unsafe_allow_html=True)

    # Final Judgment
    st.markdown("<div class='subtitle'>Final Judgment</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='judgment'>{judgment}</div>", unsafe_allow_html=True)
