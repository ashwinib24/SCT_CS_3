import re
import streamlit as st

def score_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    return score

def evaluate_password(score):
    if score == 5:
        return "💪 Strong", "green"
    elif score >= 3:
        return "⚠️ Medium", "orange"
    else:
        return "❌ Weak", "red"

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    score = score_password(password)
    strength, color = evaluate_password(score)
    
    st.markdown(f"**Score:** {score}/5")
    st.markdown(f"<h4 style='color:{color}'>{strength}</h4>", unsafe_allow_html=True)
