from langchain.prompts import (
    ChatPromptTemplate,  
    HumanMessagePromptTemplate,  
    MessagesPlaceholder,  
    SystemMessagePromptTemplate,  
)

from langchain_community.chat_message_histories import StreamlitChatMessageHistory  

from langchain_core.runnables.history import RunnableWithMessageHistory  

from langchain_google_genai import ChatGoogleGenerativeAI 

from langchain.schema.output_parser import StrOutputParser 

import streamlit as st  
from PIL import Image, ImageOps
import os
from dotenv import load_dotenv

image = Image.open("./assets/profile.jpg")


border_size = 10  
image_with_border = ImageOps.expand(image, border=border_size, fill='white')


st.image(image_with_border, width=150)

st.markdown("<h1>AI Chatbot 🚀✨ <span style='font-size:14px;'> By Areeba Bano</span></h1>", unsafe_allow_html=True)


st.markdown("🌟 Hey there!👋 I'm your AI Assistant. 🤖✨ I'm here to help you with technology, education, and general knowledge. 📚💡💻How can I assist you today? 😊🚀")

# import streamlit as st
# import google.generativeai as genai

# # API Key Load karna
# api_key = st.secrets["gemini"]["API_KEY"]

# if not api_key:
#     st.error("❌ Failed to Load Gemini API Key!")
# else:
#     genai.configure(api_key=api_key)
#     st.success("✅ Gemini API Key Loaded Successfully!")

import streamlit as st
import google.generativeai as genai

# ✅ Load API Key
api_key = st.secrets.get("gemini", {}).get("API_KEY")

if not api_key:
    st.error("❌ Failed to Load Gemini API Key!")
    st.stop()
else:
    genai.configure(api_key=api_key)
    # st.success("✅ Gemini API Key Loaded Successfully!")

# st.write("API Key from Secrets:", api_key)


# st.write("API Key from Secrets:", st.secrets.get("API_KEY"))

# # Load environment variables from .env.local
# load_dotenv(dotenv_path=".env.local")

# # # Get API Key
# # api_key = os.getenv("API_KEY")

# # if api_key:
# #     print("API Key Loaded Successfully!")
# # else:
# #     print("Failed to Load API Key!")

# api_key = st.secrets.get("API_KEY") or os.getenv("API_KEY")

# # # ✅ API Key validation
# # if not api_key:
# #     st.error("❌ Failed to Load API Key! Please check your environment variables or Streamlit secrets.")
# #     st.stop()  # Stop execution if API key is missing

# if api_key:
#     st.success("✅ API Key Loaded Successfully!")
# else:
#     st.error("❌ Failed to Load API Key!")    



prompt = ChatPromptTemplate(
    messages=[
       
        SystemMessagePromptTemplate.from_template(
            "You are a helpful AI assistant. Please respond to user queries in English, but understand the questions in English."
        ),
       
        MessagesPlaceholder(variable_name="chat_history"),
      
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)
msgs = StreamlitChatMessageHistory(key="langchain_messages")


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)


chain = prompt | model | StrOutputParser()


chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,  
    input_messages_key="question", 
    history_messages_key="chat_history",  
)


# user_input = st.text_input("", placeholder="Write your question")

col1, col2 = st.columns([4, 1])  

with col1:
    user_input = st.text_input("", placeholder="Write your question")

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀"):
        pass 


if user_input:
    
    st.chat_message("human").write(user_input)
    
   
    with st.chat_message("assistant"):
        message_placeholder = st.empty()  
        full_response = ""  

        
        config = {"configurable": {"session_id": "any"}}
        
        
        response = chain_with_history.stream({"question": user_input}, config)

        for res in response:
            full_response += res or "" 
            message_placeholder.markdown(full_response + "|")  
            message_placeholder.markdown(full_response)  

else:
    st.warning("Ask me a question❓")