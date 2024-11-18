import google.generativeai as genai
import streamlit as st

# Configure the Generative AI API key
genai.configure(api_key="AIzaSyCU4o0dyuHFZV9Bsvmg9LwxNnXEO8An6Lg")

# Page configuration
st.set_page_config(
    page_title="Advanced AI Code Reviewer",
    page_icon="🤖",
    layout="wide",
)

# Title of the app
st.title("🌟 Advanced AI Code Reviewer")

# Subtitle and description
st.subheader("AI-Powered Python Code Analysis and Suggestions")
st.markdown("""
This app leverages Google's Generative AI to review Python code for:
- **Syntax errors** ✅
- **Code improvements** 📈
- **Best practices** 🛠️

Paste your code below to get actionable insights and corrections instantly.
""")

# Input area for Python code
user_prompt = st.text_area(
    "Enter your Python code:",
    placeholder="Paste your code here...",
    height=200,
)

# Dropdown to select analysis type
analysis_type = st.selectbox(
    "Choose the type of analysis:",
    ["Error Detection", "Code Improvement Suggestions", "Full Review"],
)

# Button to generate review when clicked
if st.button("📝 Analyze Code"):
    if user_prompt.strip():
        try:
            with st.spinner("Analyzing your code..."):
                # Initialize the model
                model = genai.GenerativeModel("models/gemini-1.5-flash")

                # Start a chat session with the model
                ai_assistant = model.start_chat(history=[])

                # Prepare the prompt based on user choice
                prompt = f"Please perform {analysis_type.lower()} for the following Python code:\n\n{user_prompt}\n\nProvide detailed feedback and suggestions."
                
                # Generate the chat response
                response = ai_assistant.send_message(prompt)

                # Display the result
                st.markdown("<h2 style='color: green;'>Review Results:</h2>", unsafe_allow_html=True)
                st.text_area(
                    "Feedback and Suggestions:",
                    value=response.text,
                    height=300,
                    key="review_output",
                )
                
                # Option to download the feedback
                st.download_button(
                    label="📥 Download Feedback",
                    data=response.text,
                    file_name="code_review.txt",
                    mime="text/plain",
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter your Python code.")

# Footer
st.markdown("""
---
Made with ❤️. Powered by [Google Generative AI](https://cloud.google.com/ai).
""")
