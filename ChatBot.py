import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from streamlit_lottie import st_lottie

# Load environment variables
load_dotenv()

# Configure API Key
API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

def main():
    # Load JSON animation
    with open('bot.json', encoding='utf-8') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 200, -200)

    st.write("<h1><center>AI Chatbot - Project Assistant</center></h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>Powered by Google Gemini</p>", unsafe_allow_html=True)

    # Chatbot interface
    prompt = st.text_input("Ask anything about this project:", placeholder="Type here...", label_visibility="visible")
    model = genai.GenerativeModel("gemini-1.5-pro") 

    if st.button("SEND", use_container_width=True):
        if prompt.strip():
            try:
                # Generate response
                response = model.generate_content(prompt)
                
                # Display response
                st.write("<h3 style='color: blue;'>Response:</h3>", unsafe_allow_html=True)
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt.")
    
    # Footer
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #1e3c72;
                color: white;
                text-align: center;
                padding: 10px;
            }
        </style>
        <div class="footer">
            © IndShield Copyright
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()