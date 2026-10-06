"""
📚 Learning Hub — Python Quest + Chinese + English
Run with: streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="📚 Learning Hub",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 2.5em;
    color: #FFD700;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 15px;
    color: white;
    margin: 10px 0;
    min-height: 280px;
}
.card-green {
    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    padding: 20px;
    border-radius: 15px;
    color: white;
    margin: 10px 0;
    min-height: 280px;
}
.card-orange {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    padding: 20px;
    border-radius: 15px;
    color: white;
    margin: 10px 0;
    min-height: 280px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📚 Learning Hub</h1>', unsafe_allow_html=True)
st.markdown("### Welcome! Choose what to learn today.")

st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h2>🐍</h2>
        <h3>Python Quest</h3>
        <p>Learn Python by playing games!</p>
        <ul>
            <li>🎯 Guess the Number</li>
            <li>📝 Python Quiz</li>
            <li>🔧 Code Builder</li>
            <li>🐛 Bug Hunter</li>
            <li>🎨 Pattern Designer</li>
            <li>🤖 AI Helper</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🐍 Go to Python Quest", use_container_width=True, key="btn_python"):
        st.switch_page("pages/01_Python_Quest.py")

with col2:
    st.markdown("""
    <div class="card-green">
        <h2>📝</h2>
        <h3>中文練習</h3>
        <p>學好中文！</p>
        <ul>
            <li>📖 襯托手法</li>
            <li>📝 林肯課文分析</li>
            <li>✍️ 練習題</li>
            <li>🎮 挑戰模式</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📝 Go to 中文練習", use_container_width=True, key="btn_chinese"):
        st.switch_page("pages/02_Chinese_練習.py")

with col3:
    st.markdown("""
    <div class="card-orange">
        <h2>📝</h2>
        <h3>English</h3>
        <p>Learn English adverbs!</p>
        <ul>
            <li>📖 What are adverbs?</li>
            <li>✍️ Manner Adverbs</li>
            <li>📊 Frequency Adverbs</li>
            <li>🎮 Challenge Mode</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📝 Go to English", use_container_width=True, key="btn_english"):
        st.switch_page("pages/03_English_Adverbs.py")

st.write("---")

st.markdown("""
### 📅 Today's Learning

| Subject | Topic | Status |
|---------|-------|--------|
| 🐍 Python | Variables, Loops, Functions | ✅ Ready |
| 📝 中文 | 襯托手法（反襯） | ✅ Ready |
| 📝 English | Adverbs (manner + frequency) | ✅ Ready |

---
""")

st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
Made with ❤️ for Primary 6 learning
</div>
""", unsafe_allow_html=True)