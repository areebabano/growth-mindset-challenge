import streamlit as st
from forms.contact import contact_form

# Contact Form in Dialog
@st.dialog("📩 Contact Me")
def show_contact_form():
    contact_form()

# Hero Section  
cols1, cols2 = st.columns(2, gap="small", vertical_alignment="center")
with cols1:
    st.image("./assets/profile.png", width=300)
with cols2:
    st.title("👩‍💻 Areeba Bano", anchor=False)
    st.text("🚀 Front-End Developer | 1+ Years Experience")
    st.write(
        """
        ✨ I am a **Front-End Developer** with expertise in pixel-perfect, SEO-friendly, and responsive web applications.  
        💡 With **1+ years** of experience, I focus on delivering **high-performance, user-centric solutions** using modern web technologies.
        """
    )
    if st.button("✉ Contact Me", use_container_width=True):
        show_contact_form()

# Experience & Qualifications  
st.write("\n")
st.subheader("📌 Experience and Qualifications", anchor=False)
st.write(
    """
    ✅ 1+ years of hands-on experience in front-end development  
    ✅ Skilled in building **responsive and optimized** web applications  
    ✅ Strong foundation in modern **web technologies** and UI/UX best practices  
    ✅ Senior student in the **GIAIC program**, continuously enhancing skills  
    ✅ Passionate about delivering **high-performance solutions**  
    """
)

# Skills  
st.write("\n")
st.subheader("🚀 Skills", anchor=False)
st.write(
    """
    🔹 **Languages & Frameworks:** HTML, CSS, JavaScript, TypeScript, Next.js  
    🔹 **Front-End Development:** Responsive design, UI/UX optimization, animations  
    🔹 **Performance Optimization:** SEO best practices, lazy loading, code splitting  
    🔹 **Tools & Libraries:** Git, Tailwind CSS, Bootstrap, Figma, Inquirer.js  
    🔹 **Best Practices:** Cross-browser compatibility, accessibility, clean code  
    """
)
