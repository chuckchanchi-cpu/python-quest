"""
📝 中文練習 — 襯托手法
Run with: streamlit run chinese_chentuo.py
"""

import streamlit as st
import random

st.set_page_config(page_title="📝 中文 — 襯托手法", page_icon="📝", layout="wide")

# Custom CSS
st.markdown("""
<style>
.highlight {
    background: #fff3cd;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: bold;
}
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
.passage {
    background: #f8f9fa;
    color: #212529;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #6c757d;
    font-size: 16px;
    line-height: 1.8;
    margin: 15px 0;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.answered_q = {}

st.title("📝 中文 — 襯托手法")
st.markdown("### 學習「正襯」和「反襯」的寫作手法")

# Sidebar
with st.sidebar:
    st.header("📊 成績")
    st.metric("得分", f"{st.session_state.score}/{st.session_state.total}")
    
    st.write("---")
    st.header("📖 目錄")
    page = st.radio("選擇：", [
        "🏠 首頁",
        "📖 知識點",
        "📝 林肯課文",
        "✍️ 練習題",
        "🎮 挑戰模式"
    ])

if page == "🏠 首頁":
    st.markdown("""
    ## 歡迎！👋
    
    今天學習 **襯托手法**，一種用來突出描寫對象的寫作技巧。
    
    ### 📚 你會學到：
    
    | 內容 | 說明 |
    |------|------|
    | 📖 知識點 | 什麼是襯托？正襯和反襯的分別 |
    | 📝 林肯課文 | 分析課文中的襯托手法 |
    | ✍️ 練習題 | 鞏固所學 |
    | 🎮 挑戰模式 | 考考自己！ |
    
    ---
    
    ### 💡 今日金句：
    > 「好的襯托，就像拍照時的背景 — 背景選得好，主角就更突出。」
    """)

elif page == "📖 知識點":
    st.header("📖 知識點：什麼是襯托？")
    
    st.markdown("""
    **襯托**是一種寫作手法，通過描寫其他事物來 **突出** 主要描寫對象的特點。
    
    就像拍照時，好的背景能讓主角更突出！📸
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ 正襯")
        st.markdown("""
        用 **相似** 的事物來襯托
        
        **例子：**
        > 花園裏的花兒開得燦爛，
        > 小姑娘的笑臉更加美麗。
        
        用美麗的花 → 襯托美麗的笑臉
        """)
    
    with col2:
        st.subheader("❌ 反襯")
        st.markdown("""
        用 **相反** 的事物來襯托
        
        **例子：**
        > 教室裏吵吵鬧鬧，
        > 只有小明一個人在認真看書。
        
        用吵鬧的環境 → 襯托小明的專注
        """)
    
    st.write("---")
    
    st.subheader("🔑 反襯的關鍵詞")
    st.markdown("""
    留意這些詞語，幫助你認出「反襯」：
    
    - **但是、然而、卻、反而**
    - **其他人...但他...**
    - **大多...只有...**
    - **別人都...他卻...**
    """)
    
    st.write("---")
    
    st.subheader("📝 答題四步曲")
    st.markdown("""
    | 步驟 | 要做什麼 | 例子 |
    |------|----------|------|
    | 1️⃣ | **找人物** — 找出主要描寫的人物 | 林肯 |
    | 2️⃣ | **判類型** — 正襯還是反襯？ | 反襯 |
    | 3️⃣ | **說方法** — 用什麼襯托什麼？ | 用名門望族反襯平民出身 |
    | 4️⃣ | **講效果** — 突出了什麼？ | 突出林肯的了不起 |
    """)

elif page == "📝 林肯課文":
    st.header("📝 今日課文：林肯")
    
    st.markdown('<div class="passage">林肯是美國第十六任總統。歷任總統大多出身於名門望族，但林肯來自平民家庭。當時美國大部分參議員自認為是上流社會的、優越的人；從未料到要面對的總統是一個卑微的鞋匠的兒子。</div>', unsafe_allow_html=True)
    
    st.write("---")
    
    st.subheader("🔍 課文分析")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **主要描寫人物：** 林肯
        
        **襯托手法：** 反襯
        
        **用什麼來反襯：**
        - 其他總統 → 名門望族
        - 林肯 → 平民家庭
        - 參議員 → 上流社會
        - 林肯父親 → 卑微的鞋匠
        """)
    
    with col2:
        st.markdown("""
        **反襯效果：**
        
        通過對比「高貴」和「卑微」的出身，突出林肯雖然出身低微，卻能成為總統的 **不凡成就**。
        
        讓讀者感受到林肯的成功是靠自己的努力，而不是靠家庭背景。
        """)
    
    st.write("---")
    
    st.subheader("📝 答題示例")
    
    st.markdown("""
    **題目：** 段落怎樣運用襯托手法？
    
    **答法：**
    
    段落先寫歷任總統大多出身 **名門望族**，再寫林肯來自 **平民家庭**；
    又寫參議員自認為 **上流社會**，從未料到總統是 **卑微的鞋匠** 的兒子。
    
    通過這些「高貴」的背景，**反襯** 出林肯出身的「卑微」，
    突出他憑實力成為總統的 **了不起**。
    """)

elif page == "✍️ 練習題":
    st.header("✍️ 練習題")
    
    exercises = [
        {
            "q": "以下段落運用了哪種襯托手法？",
            "passage": "全班同學都考到90分以上，只有小明一個人不及格。",
            "options": ["正襯", "反襯"],
            "answer": "反襯",
            "explain": "用其他同學的優秀成績，反襯小明的成績差。"
        },
        {
            "q": "以下段落運用了哪種襯托手法？",
            "passage": "花園裏的玫瑰開得紅艷艷的，旁邊的百合花也開得潔白美麗。",
            "options": ["正襯", "反襯"],
            "answer": "正襯",
            "explain": "用玫瑰的美麗來襯托百合花的美麗，兩者相似。"
        },
        {
            "q": "以下段落主要描寫的人物是誰？",
            "passage": "那天的天氣非常炎熱，街上的人們都汗流浹背，紛紛躲進冷氣商店裏。但清潔工人依然頂着烈日，默默地打掃街道。",
            "options": ["街上的人們", "清潔工人", "商店裏的人"],
            "answer": "清潔工人",
            "explain": "主要描寫清潔工人在炎熱天氣下依然辛勤工作。"
        },
        {
            "q": "上面的清潔工人段落運用了什麼襯托手法？",
            "passage": "那天的天氣非常炎熱，街上的人們都汗流浹背，紛紛躲進冷氣商店裏。但清潔工人依然頂着烈日，默默地打掃街道。",
            "options": ["正襯", "反襯"],
            "answer": "反襯",
            "explain": "用人們躲進冷氣商店的行為，反襯清潔工人頂着烈日工作的精神。"
        },
        {
            "q": "以下段落運用了哪種襯托手法？",
            "passage": "房間裏安靜得連一根針掉在地上都聽得到，小華卻在專心地畫畫。",
            "options": ["正襯", "反襯"],
            "answer": "正襯",
            "explain": "用安靜的環境來襯托小華的專注，兩者方向一致。"
        },
        {
            "q": "以下段落的主要描寫對象是什麼？",
            "passage": "這家餐廳的菜式很多，有中菜、西菜、日菜，但最出名的還是它的招牌燒鵝。",
            "options": ["中菜", "西菜", "日菜", "招牌燒鵝"],
            "answer": "招牌燒鵝",
            "explain": "用其他菜式的豐富，襯托招牌燒鵝的特別和出名。"
        }
    ]
    
    if 'ex_index' not in st.session_state:
        st.session_state.ex_index = 0
        st.session_state.ex_correct = 0
        st.session_state.ex_answered = False
    
    idx = st.session_state.ex_index
    
    if idx < len(exercises):
        ex = exercises[idx]
        st.progress((idx) / len(exercises))
        st.subheader(f"第 {idx+1} 題 / 共 {len(exercises)} 題")
        
        st.write(f"**{ex['q']}**")
        st.markdown(f'<div class="passage">{ex["passage"]}</div>', unsafe_allow_html=True)
        
        if not st.session_state.ex_answered:
            answer = st.radio("選擇答案：", ex['options'], key=f"ex_{idx}")
            
            if st.button("✅ 提交", key=f"ex_submit_{idx}"):
                st.session_state.ex_answered = True
                st.session_state.total += 1
                
                if answer == ex['answer']:
                    st.session_state.ex_correct += 1
                    st.session_state.score += 1
                    st.markdown(f'<div class="correct">🎉 正確！{ex["explain"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="wrong">❌ 錯誤！答案是「{ex["answer"]}」</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="info-box">💡 {ex["explain"]}</div>', unsafe_allow_html=True)
        else:
            if st.button("➡️ 下一題", key=f"ex_next_{idx}"):
                st.session_state.ex_index += 1
                st.session_state.ex_answered = False
                st.rerun()
    else:
        st.balloons()
        st.markdown(f'<div class="correct">🏆 練習完成！答對 {st.session_state.ex_correct}/{len(exercises)} 題</div>', unsafe_allow_html=True)
        if st.button("🔄 重新練習", key="ex_retry"):
            st.session_state.ex_index = 0
            st.session_state.ex_correct = 0
            st.session_state.ex_answered = False
            st.rerun()

elif page == "🎮 挑戰模式":
    st.header("🎮 挑戰模式：寫作練習")
    
    st.markdown("""
    ### ✍️ 用「反襯」手法寫一個段落
    
    **要求：**
    - 不少於50字
    - 描寫以下其中一個人物：
      - A. 勤奮的同學
      - B. 勇敢的消防員
      - C. 慈祥的奶奶
    """)
    
    choice = st.selectbox("選擇人物：", ["A. 勤奮的同學", "B. 勇敢的消防員", "C. 慈祥的奶奶"], key="challenge_choice")
    
    user_text = st.text_area("寫你的段落：", height=150, key="challenge_text", placeholder="用反襯手法描寫...")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📝 提交作品", key="challenge_submit"):
            if len(user_text) < 10:
                st.warning("請寫多一點！")
            else:
                st.session_state.score += 2
                st.session_state.total += 1
                st.markdown(f'<div class="correct">🎉 好棒！你運用了反襯手法！+2分</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="info-box">💡 提示：檢查你的段落有沒有「對比」— 用其他人的行為來突出主角的特點。</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 💡 示例")
        st.markdown("""
        **A. 勤奮的同學：**
        
        > 下課鈴一響，同學們都衝出教室去操場玩耍，課室裏只剩下小華一個人。他安靜地坐在座位上，專心地做着數學練習，完全不理會窗外傳來的歡笑聲。
        """)