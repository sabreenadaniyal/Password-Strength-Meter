import streamlit as st
import re    # module in Python used to work with regular expressions (patterns for searching text)

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):  # Raw strings(r"...")tell Python not to treat \ as a special character.
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&#]", password):
        strength += 1
    
    if strength == 0:
        return "Very Weak", "#e74c3c", "❌", "Your Password is too short and lacks complexity!"
    elif strength == 1:
        return "Weak", "#FF5733", "⚠️", "Add more characters and different types!"
    elif strength == 2:
        return "Moderate", "#F39C12", "🟡", "Can be improved with special characters & numbers!"
    elif strength == 3:
        return "Strong", "#3498db", "🔵", "Consider making it even longer!"
    else:
        return "Very Strong", "#2ecc71", "✅", "Your password is highly secure!"

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="wide")

st.sidebar.title("⚙️ **Settings**")
st.sidebar.markdown("Use this tool to check your password strength.")
st.sidebar.markdown("### Strength Criteria:")
st.sidebar.markdown("- ✅ Minimum 8 characters")
st.sidebar.markdown("- 🔠 At least one uppercase letter")
st.sidebar.markdown("- 🔡 At least one lowercase letter")
st.sidebar.markdown("- 🔢 At least one number")
st.sidebar.markdown("- 🔣 At least one special character")

st.markdown("""
    <style>
        body {
            background-color: #1e1e2f;
            color: #ecf0f1;
            font-family: 'Arial', sans-serif;
        }
        .password-box {
            padding: 20px;
            border-radius: 12px;
            background: linear-gradient(135deg, #2c3e50, #4ca1af);
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
            color: white;
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #f1c40f;
            padding: 10px;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }
        .input-box {
            width: 100%;
            padding: 12px;
            font-size: 18px;
            border-radius: 8px;
            border: none;
            outline: none;
            box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 50px;
            color: #bdc3c7;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🔐 Password Strength Meter</div>", unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")

if password:
    strength, color, icon, message = check_password_strength(password)
    st.markdown(f"""
        <div class='password-box' style='border-left: 8px solid {color};'>
            {icon} {strength} <br> <small>{message}</small>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='footer'>
        Made with ❤️ using Streamlit | © 2025 Password Strength Meter
    </div>
""", unsafe_allow_html=True)
