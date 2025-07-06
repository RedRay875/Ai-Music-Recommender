import streamlit as st
from recommend import df, recommend_songs

# --- Page Configuration ---
st.set_page_config(
    page_title="🎧 Music Recommender",
    page_icon="🎶",
    layout="centered"
)

# --- Custom Styling ---
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        .title-text {
            text-align: center;
            font-size: 2.8rem;
            color: #333;
            margin-bottom: 0.2rem;
        }
        .subtitle-text {
            text-align: center;
            font-size: 1.1rem;
            color: #666;
            margin-bottom: 2rem;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
        }
        .stButton>button:hover {
            background-color: #e94444;
        }
        .card {
            background-color: #f9f9f9;
            padding: 1.2rem;
            border-radius: 10px;
            box-shadow: 0 0 6px rgba(0,0,0,0.05);
            margin-bottom: 1.2rem;
        }
        .lyrics {
            font-family: monospace;
            font-size: 0.9rem;
            white-space: pre-wrap;
            color: #444;
        }
        .footer {
            text-align: center;
            font-size: 0.85rem;
            color: #888;
            margin-top: 3rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='title-text'>🎧 AI Music Recommender</div>",
            unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>Get music recommendations based on lyrical meaning</div>",
            unsafe_allow_html=True)

# --- Song Selection ---
song_list = sorted(df['song'].dropna().unique())
selected_song = st.selectbox("🔍 Select a song:", song_list)

# --- Button & Recommendations ---
if st.button("🚀 Recommend Similar Songs"):
    with st.spinner("Finding similar tracks... 🎼"):
        recommendations = recommend_songs(selected_song)
        if recommendations is None:
            st.warning("❌ Song not found in the dataset.")
        else:
            st.success("🎯 Top recommendations based on lyrics:")

            # If lyrics exist, show full professional cards
            if 'text' in recommendations.columns:
                for i, row in recommendations.iterrows():
                    st.markdown(f"""
                        <div class="card">
                            <h4>{i}. {row['song']} — <span style="color:#555"><i>{row['artist']}</i></span></h4>
                            <details>
                                <summary style="cursor:pointer;">📖 Show Lyrics</summary>
                                <div class="lyrics">{row['text']}</div>
                            </details>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.dataframe(recommendations, use_container_width=True)

# --- Footer ---
st.markdown("""
    <div class="footer">
        Built with ❤️ using Python, NLP and Streamlit<br>
        <a href="https://github.com/yourusername" target="_blank">GitHub</a> | 
        <a href="https://streamlit.io" target="_blank">Streamlit</a>
    </div>
""", unsafe_allow_html=True)
