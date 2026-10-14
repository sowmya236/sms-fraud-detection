
import streamlit as st
import joblib

# Load the trained model
model = joblib.load("sms_fraud_model.pkl")

st.set_page_config(
    page_title="SMS Fraud Detection",
    page_icon="📱",
    layout="centered"
)

st.title("📱 SMS Fraud Message Detection")
st.write(
    "Enter an SMS message to check whether it may be spam "
    "or a normal message."
)

message = st.text_area(
    "Enter your SMS message:",
    placeholder="Example: Congratulations! You won a prize..."
)

if st.button("Detect Message", type="primary"):
    if not message.strip():
        st.warning("Please enter an SMS message.")
    else:
        prediction = model.predict([message])[0]

        st.subheader("Prediction Result")

        if prediction == "spam":
            st.error("⚠️ SPAM / POSSIBLE FRAUD")
            st.write(
                "This message resembles spam. Avoid clicking "
                "suspicious links or sharing personal details."
            )
        else:
            st.success("✅ LEGITIMATE / NORMAL")
            st.write(
                "The model classified this message as normal. "
                "This does not guarantee that it is safe."
            )

st.divider()
st.caption(
    "Educational project. AI predictions can be incorrect. "
    "Never share OTPs, passwords, or banking PINs."
)
