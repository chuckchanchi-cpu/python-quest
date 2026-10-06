"""
🐍 Python Quest - A Fun Game to Learn Python!
For Primary 6 students (age 11-12)
Run with: streamlit run app.py
"""

import streamlit as st
import random
import time
import json
import urllib.request

# Page config
st.set_page_config(
    page_title="🐍 Python Quest",
    page_icon="🐍",
    layout="centered"
)

# Custom CSS - fixed colors for readability
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 2.5em;
    color: #FFD700;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.score-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 15px;
    border-radius: 10px;
    color: white;
    text-align: center;
    font-size: 1.2em;
}
.code-block {
    background: #1e1e1e;
    color: #d4d4d4;
    padding: 15px;
    border-radius: 8px;
    font-family: 'Courier New', monospace;
}
.ai-explain {
    background: #1a1a2e;
    color: #e0e0e0;
    padding: 16px;
    border-radius: 10px;
    border-left: 4px solid #00d4ff;
    font-size: 15px;
    line-height: 1.7;
    margin: 10px 0;
}
.ai-explain strong {
    color: #00d4ff;
}
.ai-explain code {
    background: #2d2d44;
    color: #ffd700;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
}
.ai-header {
    color: #00d4ff;
    font-size: 1.1em;
    font-weight: bold;
}
.result-correct {
    background: #1b3a1b;
    color: #4cff4c;
    padding: 12px;
    border-radius: 8px;
    border-left: 4px solid #4cff4c;
    font-weight: bold;
    font-size: 15px;
}
.result-wrong {
    background: #3a1b1b;
    color: #ff6b6b;
    padding: 12px;
    border-radius: 8px;
    border-left: 4px solid #ff6b6b;
    font-weight: bold;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# AI Helper - Generate explanations using Silra API
# ──────────────────────────────────────────────────────────
def ai_explain(question, correct_answer, user_answer=None, is_correct=False):
    """Use AI to generate a kid-friendly explanation."""
    try:
        if is_correct:
            prompt = f"""You are teaching an 11-year-old Python. In 2-3 short sentences, explain WHY this answer is correct. Use simple words and a fun analogy.

Question: {question}
Correct Answer: {correct_answer}

Keep it simple, fun, and encouraging. No markdown headers."""
        else:
            prompt = f"""You are teaching an 11-year-old Python. In 2-3 short sentences, explain why the correct answer is right and why their choice was wrong. Use simple words and a fun analogy.

Question: {question}
Correct Answer: {correct_answer}
Their Answer: {user_answer}

Keep it simple, fun, and encouraging. No markdown headers."""

        data = json.dumps({
            "model": "qwen3.8-flash",
            "messages": [
                {"role": "system", "content": "You are a friendly Python teacher for kids. Keep answers under 60 words. Use simple language. Be encouraging."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 150,
            "temperature": 0.7
        }).encode('utf-8')

        req = urllib.request.Request(
            "https://api.silra.cn/v1/chat/completions",
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {st.secrets.get('OPENAI_API_KEY', 'sk-2Gv2HA9MJKzeCkxEZj7708Hyakis0eI5TQzq96A1xmtwZUYH')}"
            }
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode())
            return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        return None

def ai_generate_question(topic="python basics"):
    """Generate a new quiz question using AI."""
    try:
        prompt = f"""Generate ONE multiple-choice Python question for an 11-year-old beginner.
Topic: {topic}

Return ONLY valid JSON in this exact format:
{{"q": "question text", "options": ["A", "B", "C", "D"], "answer": "correct option text", "explain": "simple explanation"}}

Make it fun and age-appropriate. No markdown, just JSON."""

        data = json.dumps({
            "model": "qwen3.8-flash",
            "messages": [
                {"role": "system", "content": "You generate Python quiz questions for kids. Return only valid JSON, no markdown."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 200,
            "temperature": 0.8
        }).encode('utf-8')

        req = urllib.request.Request(
            "https://api.silra.cn/v1/chat/completions",
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {st.secrets.get('OPENAI_API_KEY', 'sk-2Gv2HA9MJKzeCkxEZj7708Hyakis0eI5TQzq96A1xmtwZUYH')}"
            }
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode())
            content = result['choices'][0]['message']['content'].strip()
            # Try to extract JSON
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            return json.loads(content)
    except Exception:
        return None

# Initialize session state - persistent across reruns
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.level = 1
    st.session_state.badges = []
    st.session_state.streak = 0
    st.session_state.total_correct = 0
    st.session_state.total_attempted = 0

# ──────────────────────────────────────────────────────────
# GAME 1: Guess the Number
# ──────────────────────────────────────────────────────────
def game_guess_number():
    st.header("🎯 Level 1: Guess the Number")
    
    with st.expander("📖 Python Code Example", expanded=False):
        st.code("""
# This is how Python looks!
secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number (1-100): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 You got it!")
""", language='python')
    
    if 'gtn_number' not in st.session_state:
        st.session_state.gtn_number = random.randint(1, 100)
        st.session_state.gtn_attempts = 0
        st.session_state.gtn_won = False
        st.session_state.gtn_history = []
    
    if not st.session_state.gtn_won:
        col1, col2 = st.columns([2, 1])
        with col1:
            guess = st.number_input("Guess a number (1-100):", min_value=1, max_value=100, value=50, key="gtn_input")
        with col2:
            st.metric("Attempts", st.session_state.gtn_attempts)
        
        if st.button("🎯 Submit Guess", key="gtn_submit"):
            st.session_state.gtn_attempts += 1
            secret = st.session_state.gtn_number
            
            if guess < secret:
                st.session_state.gtn_history.append(f"⬆️ {guess} → Too low")
                st.markdown(f'<div class="result-wrong">⬆️ {guess} is too low! Try higher.</div>', unsafe_allow_html=True)
            elif guess > secret:
                st.session_state.gtn_history.append(f"⬇️ {guess} → Too high")
                st.markdown(f'<div class="result-wrong">⬇️ {guess} is too high! Try lower.</div>', unsafe_allow_html=True)
            else:
                st.session_state.gtn_won = True
                st.session_state.gtn_history.append(f"✅ {guess} → Correct!")
                st.balloons()
                points = max(100 - (st.session_state.gtn_attempts * 10), 10)
                st.session_state.score += points
                st.session_state.total_correct += 1
                if "🎯 Guess Master" not in st.session_state.badges:
                    st.session_state.badges.append("🎯 Guess Master")
                st.markdown(f'<div class="result-correct">🎉 Got it in {st.session_state.gtn_attempts} attempts! +{points} points!</div>', unsafe_allow_html=True)
        
        if st.session_state.gtn_history:
            with st.expander("📜 Guess History"):
                for h in st.session_state.gtn_history:
                    st.write(h)
    else:
        st.markdown(f'<div class="result-correct">✅ Number was {st.session_state.gtn_number}!</div>', unsafe_allow_html=True)
        if st.button("🔄 Play Again", key="gtn_again"):
            del st.session_state.gtn_number
            del st.session_state.gtn_attempts
            del st.session_state.gtn_won
            del st.session_state.gtn_history
            st.rerun()

# ──────────────────────────────────────────────────────────
# GAME 2: Python Quiz (with AI explanations + AI questions)
# ──────────────────────────────────────────────────────────
def game_quiz():
    st.header("📝 Level 2: Python Quiz")
    
    with st.expander("📖 Python Code Example", expanded=False):
        st.code("""
# A dictionary stores key-value pairs
question = {
    "question": "What does print() do?",
    "options": ["Shows text", "Deletes files"],
    "answer": "Shows text"
}

# A function is reusable code
def check_answer(user_answer, correct):
    if user_answer == correct:
        return "Correct! 🎉"
    return "Try again! ❌"
""", language='python')
    
    questions = [
        {"q": "What does `print('Hello')` do?", "options": ["Shows 'Hello' on screen", "Deletes Hello", "Sends an email", "Creates a file"], "answer": "Shows 'Hello' on screen", "explain": "print() shows text on the screen."},
        {"q": "Which one stores a list of items?", "options": ["print()", "[1, 2, 3]", "if/else", "while"], "answer": "[1, 2, 3]", "explain": "Square brackets [] create a list."},
        {"q": "What does `if x > 10:` mean?", "options": ["Always do something", "Do something only if x is bigger than 10", "Make x bigger than 10", "Count to 10"], "answer": "Do something only if x is bigger than 10", "explain": "'if' checks a condition."},
        {"q": "How do you make a loop that counts 5 times?", "options": ["loop(5)", "for i in range(5):", "count = 5", "5 times do:"], "answer": "for i in range(5):", "explain": "'for i in range(5)' repeats code 5 times."},
        {"q": "What is a variable?", "options": ["A type of loop", "A box that stores data", "A math equation", "A Python error"], "answer": "A box that stores data", "explain": "Variables are like labeled boxes."},
        {"q": "What does `len('hello')` return?", "options": ["'hello'", "5", "0", "Error"], "answer": "5", "explain": "len() counts characters."},
        {"q": "Which is correct to define a function?", "options": ["function myFunc():", "def myFunc():", "make myFunc():", "func myFunc():"], "answer": "def myFunc():", "explain": "'def' defines a function."},
        {"q": "What will `2 ** 3` give?", "options": ["6", "8", "5", "23"], "answer": "8", "explain": "** means power. 2**3 = 8."}
    ]
    
    # AI question generation button
    if st.button("🤖 Generate AI Question", key="ai_gen_q"):
        with st.spinner("🤖 AI is creating a question..."):
            ai_q = ai_generate_question()
            if ai_q:
                questions.append(ai_q)
                st.success("🤖 New AI question added!")
                st.rerun()
            else:
                st.warning("Couldn't generate a question right now.")
    
    if 'quiz_index' not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.quiz_correct = 0
        st.session_state.quiz_answered = False
    
    idx = st.session_state.quiz_index
    
    if idx < len(questions):
        q = questions[idx]
        st.progress(idx / len(questions))
        st.subheader(f"Question {idx+1}/{len(questions)}")
        st.write(f"**{q['q']}**")
        
        answer = st.radio("Choose your answer:", q['options'], key=f"quiz_{idx}")
        
        if not st.session_state.quiz_answered:
            if st.button("✅ Submit", key=f"quiz_submit_{idx}"):
                st.session_state.quiz_answered = True
                st.session_state.total_attempted += 1
                
                if answer == q['answer']:
                    st.session_state.quiz_correct += 1
                    st.session_state.score += 20
                    st.session_state.streak += 1
                    st.session_state.total_correct += 1
                    st.markdown(f'<div class="result-correct">🎉 Correct! {q["explain"]}</div>', unsafe_allow_html=True)
                    
                    # AI explanation for correct answer
                    with st.spinner("🤖 AI generating explanation..."):
                        ai_text = ai_explain(q['q'], q['answer'], answer, True)
                        if ai_text:
                            st.markdown(f'<div class="ai-explain"><span class="ai-header">🤖 AI Teacher:</span><br>{ai_text}</div>', unsafe_allow_html=True)
                    
                    if st.session_state.streak >= 3:
                        st.info(f"🔥 {st.session_state.streak} in a row! On fire!")
                else:
                    st.session_state.streak = 0
                    st.markdown(f'<div class="result-wrong">❌ Wrong! The answer is: {q["answer"]}</div>', unsafe_allow_html=True)
                    st.info(f"💡 {q['explain']}")
                    
                    # AI explanation for wrong answer
                    with st.spinner("🤖 AI generating explanation..."):
                        ai_text = ai_explain(q['q'], q['answer'], answer, False)
                        if ai_text:
                            st.markdown(f'<div class="ai-explain"><span class="ai-header">🤖 AI Teacher:</span><br>{ai_text}</div>', unsafe_allow_html=True)
        else:
            if st.button("➡️ Next Question", key=f"quiz_next_{idx}"):
                st.session_state.quiz_index += 1
                st.session_state.quiz_answered = False
                st.rerun()
    else:
        st.balloons()
        score = st.session_state.quiz_correct
        st.markdown(f'<div class="result-correct">🏆 Quiz Complete! {score}/{len(questions)} correct!</div>', unsafe_allow_html=True)
        if score >= 6 and "📝 Quiz Master" not in st.session_state.badges:
            st.session_state.badges.append("📝 Quiz Master")
        if st.button("🔄 Retry Quiz", key="quiz_retry"):
            st.session_state.quiz_index = 0
            st.session_state.quiz_correct = 0
            st.session_state.quiz_answered = False
            st.session_state.streak = 0
            st.rerun()

# ──────────────────────────────────────────────────────────
# GAME 3: Code Builder
# ──────────────────────────────────────────────────────────
def game_code_builder():
    st.header("🔧 Level 3: Code Builder")
    
    st.write("**Put the code lines in the correct order!**")
    
    challenges = [
        {"title": "Make a greeting program", "lines": ['name = "Alice"', 'print("Hello, " + name + "!")', 'print("Welcome to Python!")'], "correct_order": [0, 2, 1], "hint": "First set the name, then welcome, then greet"},
        {"title": "Count from 1 to 5", "lines": ['for i in range(1, 6):', '    print(i)', 'print("Done counting!")'], "correct_order": [0, 1, 2], "hint": "Set up the loop, print inside the loop, then print after"},
        {"title": "Check if number is positive", "lines": ['x = 10', 'if x > 0:', '    print("Positive!")', 'else:', '    print("Negative!")'], "correct_order": [0, 1, 2, 3, 4], "hint": "Set x, check condition, handle both cases"},
        {"title": "Create and use a function", "lines": ['def add(a, b):', '    return a + b', 'result = add(3, 5)', 'print(result)'], "correct_order": [0, 1, 2, 3], "hint": "Define function, return value, call it, print result"}
    ]
    
    if 'cb_index' not in st.session_state:
        st.session_state.cb_index = 0
        st.session_state.cb_completed = []
    
    idx = st.session_state.cb_index
    
    if idx < len(challenges):
        ch = challenges[idx]
        st.subheader(f"Challenge {idx+1}/{len(challenges)}: {ch['title']}")
        st.progress(idx / len(challenges))
        
        if f"cb_shuffled_{idx}" not in st.session_state:
            shuffled = list(range(len(ch['lines'])))
            random.shuffle(shuffled)
            st.session_state[f"cb_shuffled_{idx}"] = shuffled
        
        shuffled = st.session_state[f"cb_shuffled_{idx}"]
        
        user_order = []
        for i, pos in enumerate(shuffled):
            selected = st.selectbox(f"Position {i+1}:", options=list(range(len(ch['lines']))), format_func=lambda x: ch['lines'][x], key=f"cb_select_{idx}_{i}", index=0)
            user_order.append(selected)
        
        st.info(f"💡 Hint: {ch['hint']}")
        
        if st.button("✅ Check Order", key=f"cb_check_{idx}"):
            if user_order == ch['correct_order']:
                st.session_state.score += 30
                st.session_state.cb_completed.append(idx)
                if "🔧 Code Builder" not in st.session_state.badges:
                    st.session_state.badges.append("🔧 Code Builder")
                st.markdown('<div class="result-correct">🎉 Perfect order!</div>', unsafe_allow_html=True)
                st.code('\n'.join(ch['lines']), language='python')
            else:
                st.markdown('<div class="result-wrong">❌ Not quite right. Try again!</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if idx > 0 and st.button("⬅️ Previous", key="cb_prev"):
                st.session_state.cb_index -= 1
                st.rerun()
        with col2:
            if st.button("➡️ Next Challenge", key="cb_next"):
                st.session_state.cb_index += 1
                st.rerun()
    else:
        st.balloons()
        st.markdown(f'<div class="result-correct">🏆 All {len(challenges)} challenges completed!</div>', unsafe_allow_html=True)
        if st.button("🔄 Retry", key="cb_retry"):
            st.session_state.cb_index = 0
            st.session_state.cb_completed = []
            st.rerun()

# ──────────────────────────────────────────────────────────
# GAME 4: Bug Hunter
# ──────────────────────────────────────────────────────────
def game_bug_hunter():
    st.header("🐛 Level 4: Bug Hunter")
    
    st.write("**Find the bug in the code!**")
    
    bugs = [
        {"buggy": 'print("Hello World")', "correct": 'print("Hello World")', "bug_type": "no_bug", "hint": "This one is actually correct!", "explanation": "Sometimes code is correct! Always check carefully."},
        {"buggy": 'prnt("Hello")', "correct": 'print("Hello")', "bug_type": "typo", "hint": "Look at the function name...", "explanation": "print() has an 'i' in it! Typos are the #1 bug."},
        {"buggy": 'if x = 5:\n    print("five")', "correct": 'if x == 5:\n    print("five")', "bug_type": "operator", "hint": "How do you CHECK equality?", "explanation": "= assigns. == checks equality."},
        {"buggy": 'for i in range(5)\n    print(i)', "correct": 'for i in range(5):\n    print(i)', "bug_type": "missing_colon", "hint": "What's missing at end of the for line?", "explanation": "Python needs a colon (:) after for, if, while, def!"},
        {"buggy": 'name = "Bob"\nprint("Hello " + name)', "correct": 'name = "Bob"\nprint("Hello " + name)', "bug_type": "no_bug", "hint": "Is this actually wrong?", "explanation": "This is correct! String concatenation with + works."},
        {"buggy": 'x = 10\ny = 3\nprint(x / y)', "correct": 'x = 10\ny = 3\nprint(x // y)', "bug_type": "division", "hint": "Whole number or decimal?", "explanation": "/ gives decimal. // gives whole number."},
        {"buggy": 'numbers = [1, 2, 3]\nprint(numbers[3])', "correct": 'numbers = [1, 2, 3]\nprint(numbers[2])', "bug_type": "index", "hint": "Lists start counting from...", "explanation": "Lists start at 0! [1,2,3] has indices 0,1,2."},
        {"buggy": 'def greet(name)\n    print("Hi " + name)', "correct": 'def greet(name):\n    print("Hi " + name)', "bug_type": "missing_colon", "hint": "What goes after def?", "explanation": "def lines need a colon (:) at the end!"}
    ]
    
    if 'bh_index' not in st.session_state:
        st.session_state.bh_index = 0
        st.session_state.bh_correct = 0
        st.session_state.bh_answered = False
    
    idx = st.session_state.bh_index
    
    if idx < len(bugs):
        bug = bugs[idx]
        st.subheader(f"Bug {idx+1}/{len(bugs)}")
        st.progress(idx / len(bugs))
        
        st.code(bug['buggy'], language='python')
        
        if not st.session_state.bh_answered:
            choice = st.radio("Is there a bug?", ["🐛 Yes, there's a bug!", "✅ This code is correct!"], key=f"bh_{idx}")
            
            if st.button("🔍 Check", key=f"bh_check_{idx}"):
                st.session_state.bh_answered = True
                st.session_state.total_attempted += 1
                is_correct = (choice.startswith("🐛") and bug['bug_type'] != "no_bug") or (choice.startswith("✅") and bug['bug_type'] == "no_bug")
                
                if is_correct:
                    st.session_state.bh_correct += 1
                    st.session_state.score += 25
                    st.session_state.total_correct += 1
                    st.markdown(f'<div class="result-correct">🎉 Correct! {bug["explanation"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="result-wrong">❌ {bug["explanation"]}</div>', unsafe_allow_html=True)
                
                if bug['bug_type'] != "no_bug":
                    st.code(bug['correct'], language='python')
                    st.caption("✅ Fixed version")
                
                # AI explanation
                with st.spinner("🤖 AI explaining..."):
                    ai_text = ai_explain(f"Find the bug: {bug['buggy']}", bug['correct'], choice, is_correct)
                    if ai_text:
                        st.markdown(f'<div class="ai-explain"><span class="ai-header">🤖 AI Teacher:</span><br>{ai_text}</div>', unsafe_allow_html=True)
        else:
            if st.button("➡️ Next Bug", key=f"bh_next_{idx}"):
                st.session_state.bh_index += 1
                st.session_state.bh_answered = False
                st.rerun()
    else:
        st.balloons()
        score = st.session_state.bh_correct
        st.markdown(f'<div class="result-correct">🏆 Bug Hunt Complete! Found {score}/{len(bugs)} correctly!</div>', unsafe_allow_html=True)
        if score >= 6 and "🐛 Bug Hunter" not in st.session_state.badges:
            st.session_state.badges.append("🐛 Bug Hunter")
        if st.button("🔄 Retry", key="bh_retry"):
            st.session_state.bh_index = 0
            st.session_state.bh_correct = 0
            st.session_state.bh_answered = False
            st.rerun()

# ──────────────────────────────────────────────────────────
# GAME 5: Pattern Designer
# ──────────────────────────────────────────────────────────
def game_drawing():
    st.header("🎨 Level 5: Pattern Designer")
    
    with st.expander("📖 Python Code Example", expanded=False):
        st.code("""
import turtle

for i in range(4):
    t.forward(100)
    t.right(90)
# This draws a square!
""", language='python')
    
    pattern = st.selectbox("Choose a pattern:", ["Square", "Triangle", "Star", "Circle Spiral", "Diamond"], key="draw_pattern")
    size = st.slider("Size:", 50, 200, 100, key="draw_size")
    color = st.color_picker("Color:", "#FF6B6B", key="draw_color")
    
    code_templates = {
        "Square": f"""import turtle
t = turtle.Turtle()
t.color("{color}")
for i in range(4):
    t.forward({size})
    t.right(90)
turtle.done()""",
        "Triangle": f"""import turtle
t = turtle.Turtle()
t.color("{color}")
for i in range(3):
    t.forward({size})
    t.right(120)
turtle.done()""",
        "Star": f"""import turtle
t = turtle.Turtle()
t.color("{color}")
for i in range(5):
    t.forward({size})
    t.right(144)
turtle.done()""",
        "Circle Spiral": f"""import turtle
t = turtle.Turtle()
t.color("{color}")
for i in range(20):
    t.circle({size} - i * 5)
    t.right(18)
turtle.done()""",
        "Diamond": f"""import turtle
t = turtle.Turtle()
t.color("{color}")
for i in range(4):
    t.forward({size})
    if i % 2 == 0:
        t.right(60)
    else:
        t.right(120)
turtle.done()"""
    }
    
    st.code(code_templates[pattern], language='python')
    
    st.markdown("""
    **How to run this:**
    1. Copy the code above
    2. Open IDLE (comes with Python)
    3. Paste and press F5
    4. Watch the magic! ✨
    """)
    
    if st.button("✅ I ran it! (+20 points)", key="draw_done"):
        st.session_state.score += 20
        if "🎨 Pattern Designer" not in st.session_state.badges:
            st.session_state.badges.append("🎨 Pattern Designer")
        st.balloons()
        st.markdown('<div class="result-correct">🎉 Great job! You\'re a Python artist!</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# AI Chatbot - Ask anything about Python
# ──────────────────────────────────────────────────────────
def ai_chatbot():
    st.header("🤖 AI Python Helper")
    st.write("Ask me anything about Python! I'll explain it in a way that's easy to understand.")
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for msg in st.session_state.chat_history:
        if msg['role'] == 'user':
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f'<div class="ai-explain"><span class="ai-header">🤖 AI Teacher:</span><br>{msg["content"]}</div>', unsafe_allow_html=True)
    
    # Input
    user_input = st.text_input("Ask a Python question:", key="chat_input", placeholder="e.g., What is a list?")
    
    if st.button("💬 Ask", key="chat_ask") and user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        with st.spinner("🤖 Thinking..."):
            try:
                data = json.dumps({
                    "model": "qwen3.8-flash",
                    "messages": [
                        {"role": "system", "content": "You are a friendly Python teacher for an 11-year-old. Keep answers under 100 words. Use simple language, fun analogies, and code examples. Be encouraging."},
                        {"role": "user", "content": user_input}
                    ],
                    "max_tokens": 250,
                    "temperature": 0.7
                }).encode('utf-8')
                
                req = urllib.request.Request(
                    "https://api.silra.cn/v1/chat/completions",
                    data=data,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {st.secrets.get('OPENAI_API_KEY', 'sk-2Gv2HA9MJKzeCkxEZj7708Hyakis0eI5TQzq96A1xmtwZUYH')}"
                    }
                )
                with urllib.request.urlopen(req, timeout=15) as resp:
                    result = json.loads(resp.read().decode())
                    answer = result['choices'][0]['message']['content'].strip()
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})
                    st.rerun()
            except Exception as e:
                st.error(f"Couldn't reach AI: {e}")
    
    if st.button("🗑️ Clear Chat", key="chat_clear"):
        st.session_state.chat_history = []
        st.rerun()

# ──────────────────────────────────────────────────────────
# MAIN APP
# ──────────────────────────────────────────────────────────
def main():
    st.markdown('<h1 class="main-title">🐍 Python Quest 🐍</h1>', unsafe_allow_html=True)
    st.markdown("### Learn Python by playing games! 🎮")
    
    # Sidebar
    with st.sidebar:
        st.header("📊 Your Progress")
        st.markdown(f"""
        <div class="score-box">
            <h2>⭐ {st.session_state.score} Points</h2>
            <p>Level {st.session_state.level}</p>
            <p>✅ {st.session_state.total_correct}/{st.session_state.total_attempted} correct</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        
        if st.session_state.badges:
            st.header("🏆 Badges")
            for badge in st.session_state.badges:
                st.write(f"  {badge}")
        else:
            st.header("🏆 Badges")
            st.write("  Play games to earn badges!")
        
        st.write("---")
        st.header("🎮 Games")
        game = st.radio("Choose a game:", [
            "🏠 Home",
            "🎯 Guess the Number",
            "📝 Python Quiz",
            "🔧 Code Builder",
            "🐛 Bug Hunter",
            "🎨 Pattern Designer",
            "🤖 AI Helper"
        ], key="game_select")
        
        st.write("---")
        st.markdown("""
        **💡 Tips:**
        - Each game teaches Python skills
        - Earn points and badges
        - AI explains every answer!
        - Ask AI anything in AI Helper
        """)
    
    if game == "🏠 Home":
        show_home()
    elif game == "🎯 Guess the Number":
        game_guess_number()
    elif game == "📝 Python Quiz":
        game_quiz()
    elif game == "🔧 Code Builder":
        game_code_builder()
    elif game == "🐛 Bug Hunter":
        game_bug_hunter()
    elif game == "🎨 Pattern Designer":
        game_drawing()
    elif game == "🤖 AI Helper":
        ai_chatbot()

def show_home():
    st.markdown("""
    ## Welcome to Python Quest! 🐍🎮
    
    Learn Python programming by playing **6 fun activities**:
    
    | Game | What You'll Learn | Difficulty |
    |------|-------------------|------------|
    | 🎯 Guess the Number | Variables, Input, Loops | ⭐ |
    | 📝 Python Quiz | Lists, Functions, Print | ⭐⭐ |
    | 🔧 Code Builder | Code Order, Syntax | ⭐⭐ |
    | 🐛 Bug Hunter | Debugging, Errors | ⭐⭐⭐ |
    | 🎨 Pattern Designer | Loops, Turtle Graphics | ⭐⭐ |
    | 🤖 AI Helper | Ask anything! | Any |
    
    ---
    
    ### 🚀 Ready to start?
    
    Pick a game from the sidebar and begin your Python adventure!
    
    **New:** 🤖 AI Teacher explains every answer and you can ask it anything!
    """)

if __name__ == "__main__":
    main()