import streamlit as st
import re

def check_password_strength(password):
    """
    Checks password strength based on:
    - Length (8+ characters)
    - Upper & Lowercase letters
    - At least one digit (0-9)
    - At least one special character (!@#$%^&*)
    """
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("❌ Use at least 8 characters.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one lowercase letter.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("❌ Include at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 5:
        strength = "🟢 Strong Password!"
        color = "green"
    elif 3 <= score <= 4:
        strength = "🟡 Moderate Password - Consider improving it."
        color = "orange"
    else:
        strength = "🔴 Weak Password - Improve it using the suggestions below."
        color = "red"

    return strength, color, suggestions

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter a password to check its strength and get suggestions to improve it.")

# User Input
password = st.text_input("Enter your password:", type="password")

if password:
    strength, color, suggestions = check_password_strength(password)

    # Display Strength Result
    st.markdown(f"<h4 style='color: {color};'>{strength}</h4>", unsafe_allow_html=True)

    # Show Improvement Suggestions
    if suggestions:
        st.subheader("🔧 Suggestions to Improve:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")

