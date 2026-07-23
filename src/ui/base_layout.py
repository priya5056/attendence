import streamlit as st


def style_background_home():
    st.markdown("""
    <style>

        .stApp {
            background: #182f33 !important;
        }

        .stApp div[data-testid="stColumn"]{
            background-color: #e1eef7 !important;
            padding: 2.5rem !important;
            border-radius: 2rem !important;
        }

    </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
    <style>

        .stApp {
            background: #E0E3FF !important;
        }

    </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Bona+Nova+SC:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    /* ---------------- Hide Streamlit UI ---------------- */

    #MainMenu,
    footer,
    header {
        visibility: hidden;
    }

    .block-container{
        padding-top:1.5rem !important;
    }

    /* ---------------- Headings ---------------- */

    h1{
        font-family:'Bona Nova SC',serif !important;
        font-size:3.5rem !important;
        line-height:1.1 !important;
        color:#111 !important;
        margin-bottom:0rem !important;
    }

    h2{
        font-family:'Bona Nova SC',serif !important;
        font-size:2rem !important;
        color:#111 !important;
        margin-bottom:0rem !important;
    }

    h3,h4,h5,h6{
        font-family:'Outfit',sans-serif !important;
        color:#111 !important;
    }

    /* ---------------- Text ---------------- */

    p{
        font-family:'Outfit',sans-serif !important;
        color:#111 !important;
    }

    label{
        color:#111 !important;
        font-family:'Outfit',sans-serif !important;
    }

    /* Markdown */

    [data-testid="stMarkdownContainer"]{
        color:#111 !important;
        font-family:'Outfit',sans-serif !important;
    }

    [data-testid="stMarkdownContainer"] p{
        color:#111 !important;
    }

    /* Text Input */

    input,
    textarea{
        color:#111 !important;
    }

    /* Selectbox */

    [data-baseweb="select"]{
        color:#111 !important;
    }

    /* Expander */

    details,
    summary{
        color:#111 !important;
    }

    /* Alerts */

    [data-testid="stAlertContainer"]{
        color:#111 !important;
    }

    [data-testid="stAlertContainer"] *{
        color:#111 !important;
    }

    /* ---------------- Buttons ---------------- */

    button{
        border-radius:1.5rem !important;
        background:#5865F2 !important;
        color:white !important;
        border:none !important;
        padding:10px 20px !important;
        transition:all .25s ease;
    }

    button:hover{
        transform:scale(1.05);
    }

    button[kind="secondary"]{
        background:#EB459E !important;
        color:white !important;
    }

    button[kind="tertiary"]{
        background:#111 !important;
        color:white !important;
    }

    /* ---------------- Metric ---------------- */

    [data-testid="stMetricValue"]{
        color:#111 !important;
    }

    [data-testid="stMetricLabel"]{
        color:#111 !important;
    }

    /* ---------------- Tabs ---------------- */

    button[role="tab"]{
        color:#111 !important;
    }

    /* ---------------- Radio ---------------- */

    [data-testid="stRadio"] label{
        color:#111 !important;
    }

    /* ---------------- Checkbox ---------------- */

    [data-testid="stCheckbox"] label{
        color:#111 !important;
    }

    </style>
    """, unsafe_allow_html=True)
