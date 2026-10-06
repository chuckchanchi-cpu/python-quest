"""
📝 英文練習 — Adverbs 副詞
Run with: streamlit run english_adverbs.py
"""

import streamlit as st
import random

st.set_page_config(page_title="📝 English — Adverbs", page_icon="📝", layout="wide")

st.markdown("""
<style>
.correct {
    background: #d4edda;
    color: #155724;
    padding: 12px;
    border-radius: 8px;
    border-left: 4px solid #28a745;
    font-weight: bold;
    font-size: 15px;
}
.wrong {
    background: #f8d7da;
    color: #721c24;
    padding: 12px;
    border-radius: 8px;
    border-left: 4px solid #dc3545;
    font-weight: bold;
    font-size: 15px;
}
.info-box {
    background: #d1ecf1;
    color: #0c5460;
    padding: 12px;
    border-radius: 8px;
    border-left: 4px solid #17a2b8;
    font-size: 15px;
}
.freq-bar {
    height: 20px;
    border-radius: 10px;
    margin: 5px 0;
}
</style>
""", unsafe_allow_html=True)

if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.total = 0

st.title("📝 English — Adverbs 副詞")
st.markdown("### Learn how to describe verbs!")

with st.sidebar:
    st.header("📊 Score")
    st.metric("Points", f"{st.session_state.score}/{st.session_state.total}")
    
    st.write("---")
    page = st.radio("Choose:", [
        "🏠 Home",
        "📖 Learn",
        "✍️ Manner Adverbs",
        "📊 Frequency Adverbs",
        "🎮 Challenge"
    ])

if page == "🏠 Home":
    st.markdown("""
    ## Welcome! 👋
    
    Today we learn **Adverbs** — words that describe **how** an action is done.
    
    ### 📚 Topics:
    
    | Topic | What You'll Learn |
    |-------|-------------------|
    | 📖 Learn | What are adverbs? |
    | ✍️ Manner Adverbs | carefully, fast, well, early, hard |
    | 📊 Frequency Adverbs | always, usually, often, sometimes, seldom, never |
    | 🎮 Challenge | Test yourself! |
    
    ---
    
    ### 💡 Key Rule:
    > **Adverbs describe verbs.**
    > - She sings **beautifully**. (How does she sing?)
    > - He runs **fast**. (How does he run?)
    """)

elif page == "📖 Learn":
    st.header("📖 What is an Adverb?")
    
    st.markdown("""
    An **adverb** describes **how** an action is done. It tells us more about the **verb**.
    
    > We use adverbs to describe verbs.
    """)
    
    st.write("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✍️ Manner Adverbs")
        st.markdown("Tell us **how** something happens:")
        
        st.markdown("""
        | Adverb | 中文 | Example |
        |--------|------|---------|
        | carefully | 小心地 | She draws carefully. |
        | fast | 快地 | The rabbit runs fast. |
        | well | 好地 | He plays well. |
        | early | 早地 | I wake up early. |
        | hard | 努力地 | We study hard. |
        """)
    
    with col2:
        st.subheader("📊 Frequency Adverbs")
        st.markdown("Tell us **how often** something happens:")
        
        st.markdown("""
        | Adverb | % | 中文 |
        |--------|---|------|
        | always | 100% | 總是 |
        | usually | ~80% | 通常 |
        | often | ~60% | 經常 |
        | sometimes | ~40% | 有時 |
        | seldom | ~10% | 很少 |
        | never | 0% | 從不 |
        """)
    
    st.write("---")
    
    st.subheader("📍 Word Order")
    st.markdown("""
    **Manner adverbs** → after the verb
    - She sings **beautifully**.
    
    **Frequency adverbs** → before the verb
    - I **always** eat breakfast.
    
    **Time adverbs** → at the end
    - He wakes up **early**.
    """)
    
    st.write("---")
    
    st.subheader("⚠️ Common Mistakes")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ❌ She sings **beautiful**.
        (adjective, not adverb)
        """)
    with col2:
        st.markdown("""
        ✅ She sings **beautifully**.
        (adverb describes the verb)
        """)

elif page == "✍️ Manner Adverbs":
    st.header("✍️ Manner Adverbs Practice")
    
    exercises = [
        {"sentence": "The rabbit runs _______.", "answer": "fast", "hint": "The rabbit is quick!"},
        {"sentence": "We should study _______ for the exam.", "answer": "hard", "hint": "Put in effort!"},
        {"sentence": "She always does her homework _______.", "answer": "carefully", "hint": "She is very careful."},
        {"sentence": "My father wakes up _______ in the morning.", "answer": "early", "hint": "Before 7am!"},
        {"sentence": "Lily got full marks. She did _______.", "answer": "well", "hint": "She performed great!"},
        {"sentence": "Please read the instructions _______.", "answer": "carefully", "hint": "Don't make mistakes!"},
        {"sentence": "The snail moves very _______.", "answer": "slowly", "hint": "The opposite of fast."},
        {"sentence": "He plays the piano _______.", "answer": "well", "hint": "He is talented!"},
    ]
    
    if 'ma_index' not in st.session_state:
        st.session_state.ma_index = 0
        st.session_state.ma_correct = 0
        st.session_state.ma_answered = False
    
    idx = st.session_state.ma_index
    
    if idx < len(exercises):
        ex = exercises[idx]
        st.progress(idx / len(exercises))
        st.subheader(f"Question {idx+1}/{len(exercises)}")
        
        st.write(f"**{ex['sentence']}**")
        
        options = ["carefully", "fast", "well", "early", "hard", "slowly"]
        answer = st.selectbox("Choose the adverb:", options, key=f"ma_{idx}")
        
        st.info(f"💡 Hint: {ex['hint']}")
        
        if not st.session_state.ma_answered:
            if st.button("✅ Submit", key=f"ma_submit_{idx}"):
                st.session_state.ma_answered = True
                st.session_state.total += 1
                
                if answer == ex['answer']:
                    st.session_state.ma_correct += 1
                    st.session_state.score += 1
                    st.markdown(f'<div class="correct">🎉 Correct! "{ex["answer"]}" is the right answer.</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="wrong">❌ The answer is "{ex["answer"]}".</div>', unsafe_allow_html=True)
        else:
            if st.button("➡️ Next", key=f"ma_next_{idx}"):
                st.session_state.ma_index += 1
                st.session_state.ma_answered = False
                st.rerun()
    else:
        st.balloons()
        st.markdown(f'<div class="correct">🏆 Done! {st.session_state.ma_correct}/{len(exercises)} correct!</div>', unsafe_allow_html=True)
        if st.button("🔄 Retry", key="ma_retry"):
            st.session_state.ma_index = 0
            st.session_state.ma_correct = 0
            st.session_state.ma_answered = False
            st.rerun()

elif page == "📊 Frequency Adverbs":
    st.header("📊 Frequency Adverbs Practice")
    
    st.markdown("""
    ### How often?
    
    | Adverb | Frequency | Bar |
    |--------|-----------|-----|
    | always | 100% | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 |
    | usually | ~80% | 🟩🟩🟩🟩🟩🟩🟩🟩 |
    | often | ~60% | 🟩🟩🟩🟩🟩🟩 |
    | sometimes | ~40% | 🟩🟩🟩🟩 |
    | seldom | ~10% | 🟩 |
    | never | 0% | — |
    """)
    
    st.write("---")
    
    exercises = [
        {"q": "I _______ eat breakfast. I eat it every single day.", "answer": "always", "explain": "Every day = 100% = always"},
        {"q": "She _______ goes to bed late. She always sleeps early.", "answer": "never", "explain": "Always sleeps early = she NEVER goes to bed late"},
        {"q": "He _______ plays video games — maybe once a month.", "answer": "seldom", "explain": "Once a month = very few times = seldom"},
        {"q": "We _______ go to the beach in summer — about twice a month.", "answer": "often", "explain": "Twice a month = quite frequent = often"},
        {"q": "They _______ miss school. They are always present.", "answer": "never", "explain": "Always present = they NEVER miss school"},
        {"q": "I _______ eat sushi. I don't like raw fish at all.", "answer": "never", "explain": "Don't like it at all = NEVER eat it"},
        {"q": "She _______ walks to school. She takes the bus most days.", "answer": "seldom", "explain": "Most days by bus = seldom walks"},
        {"q": "He _______ plays football — about 4 times a week!", "answer": "often", "explain": "4 times a week = often"},
    ]
    
    if 'fa_index' not in st.session_state:
        st.session_state.fa_index = 0
        st.session_state.fa_correct = 0
        st.session_state.fa_answered = False
    
    idx = st.session_state.fa_index
    
    if idx < len(exercises):
        ex = exercises[idx]
        st.progress(idx / len(exercises))
        st.subheader(f"Question {idx+1}/{len(exercises)}")
        
        st.write(f"**{ex['q']}**")
        
        options = ["always", "usually", "often", "sometimes", "seldom", "never"]
        answer = st.selectbox("Choose:", options, key=f"fa_{idx}")
        
        if not st.session_state.fa_answered:
            if st.button("✅ Submit", key=f"fa_submit_{idx}"):
                st.session_state.fa_answered = True
                st.session_state.total += 1
                
                if answer == ex['answer']:
                    st.session_state.fa_correct += 1
                    st.session_state.score += 1
                    st.markdown(f'<div class="correct">🎉 Correct! {ex["explain"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="wrong">❌ Answer: "{ex["answer"]}". {ex["explain"]}</div>', unsafe_allow_html=True)
        else:
            if st.button("➡️ Next", key=f"fa_next_{idx}"):
                st.session_state.fa_index += 1
                st.session_state.fa_answered = False
                st.rerun()
    else:
        st.balloons()
        st.markdown(f'<div class="correct">🏆 Done! {st.session_state.fa_correct}/{len(exercises)} correct!</div>', unsafe_allow_html=True)
        if st.button("🔄 Retry", key="fa_retry"):
            st.session_state.fa_index = 0
            st.session_state.fa_correct = 0
            st.session_state.fa_answered = False
            st.rerun()

elif page == "🎮 Challenge":
    st.header("🎮 Adverb Challenge")
    
    st.markdown("""
    ### Mixed Practice!
    
    Fill in the blank with the correct adverb.
    """)
    
    mixed = [
        {"q": "The cheetah runs very _______.", "answer": "fast", "options": ["fast", "slowly", "carefully"]},
        {"q": "I _______ brush my teeth before bed.", "answer": "always", "options": ["never", "always", "seldom"]},
        {"q": "She completed the puzzle _______.", "answer": "carefully", "options": ["hard", "carefully", "early"]},
        {"q": "He _______ eats vegetables. He hates them!", "answer": "never", "options": ["always", "usually", "never"]},
        {"q": "The train arrived _______. We had to wait.", "answer": "early", "options": ["well", "fast", "early"]},
        {"q": "She sings _______. She should join a choir!", "answer": "well", "options": ["well", "hard", "fast"]},
        {"q": "We _______ have pizza on Fridays.", "answer": "usually", "options": ["never", "seldom", "usually"]},
        {"q": "He works _______ to support his family.", "answer": "hard", "options": ["fast", "hard", "carefully"]},
    ]
    
    if 'mx_index' not in st.session_state:
        st.session_state.mx_index = 0
        st.session_state.mx_correct = 0
        st.session_state.mx_answered = False
    
    idx = st.session_state.mx_index
    
    if idx < len(mixed):
        ex = mixed[idx]
        st.progress(idx / len(mixed))
        st.subheader(f"Question {idx+1}/{len(mixed)}")
        
        st.write(f"**{ex['q']}**")
        
        answer = st.radio("Choose:", ex['options'], key=f"mx_{idx}")
        
        if not st.session_state.mx_answered:
            if st.button("✅ Submit", key=f"mx_submit_{idx}"):
                st.session_state.mx_answered = True
                st.session_state.total += 1
                
                if answer == ex['answer']:
                    st.session_state.mx_correct += 1
                    st.session_state.score += 1
                    st.markdown(f'<div class="correct">🎉 Correct!</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="wrong">❌ Answer: "{ex["answer"]}"</div>', unsafe_allow_html=True)
        else:
            if st.button("➡️ Next", key=f"mx_next_{idx}"):
                st.session_state.mx_index += 1
                st.session_state.mx_answered = False
                st.rerun()
    else:
        st.balloons()
        st.markdown(f'<div class="correct">🏆 Challenge Complete! {st.session_state.mx_correct}/{len(mixed)} correct!</div>', unsafe_allow_html=True)
        if st.button("🔄 Retry", key="mx_retry"):
            st.session_state.mx_index = 0
            st.session_state.mx_correct = 0
            st.session_state.mx_answered = False
            st.rerun()