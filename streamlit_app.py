import streamlit as st

about_page = st.Page(
    page = "views/about_me.py",
    title = "About Me",
    icon = ":material/account_circle:",
    default = True
)

project_1_page = st.Page(
    page = "views/challenge.py",
    title = "Challenges",
    icon = ":material/trophy:",
)

project_2_page = st.Page(
    page = "views/chatbot.py",
    title = "ChatBot",
    icon = ":material/smart_toy:",
    )

# pg = st.navigation(pages=[about_page, project_1_page ,project_2_page])

pg = st.navigation(
    {
        "Personal Info" : [about_page],
        "Projects" : [project_1_page, project_2_page],
    }
)

st.logo("assets/mylogo.jpg")
st.sidebar.text("created by 𝓐𝓻𝓮𝓮𝓫𝓪 💗")

pg.run()