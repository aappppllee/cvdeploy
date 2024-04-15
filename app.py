from pathlib import Path
import base64
import streamlit as st
from PIL import Image



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
image_url = 'https://easydrawingguides.com/wp-content/uploads/2022/08/cartoon-face-11.png'

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Arjun Sharma"
PAGE_ICON = ":wave:"
NAME = "Arjun Sharma"
DESCRIPTION = """
 Actively seeking a role in Data Science and Software Engineering to apply my analytical skills and knowledge in real-world
 scenarios, aiming to contribute significantly to the organization.
"""
EMAIL = "s.arjun1482@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/aappppllee",
    "Leetcode": "https://leetcode.com/spurnendu1482000/",
    "LinkedIn": "https://www.linkedin.com/in/gradientdescent/",
    "YouTube": "https://www.youtube.com/watch?v=bk-w8pK_yrI&list=PL44Kg_kF9XpNZrsNO3zBze6_tjGwzno8Y&index=5"
}
PROJECTS = {
    "🏆 Amex Credit Card Recommendation - System to suggest credit cards to users from merchant based on their spending habits and preferences ": "https://github.com/aappppllee/amexcard",
    "🏆 Notes keeping app like sticker board": "https://github.com/aappppllee/keeperapp2",
    "🏆 Using GCP Message Broker(Pub/Sub) to processes recently uploaded file and count its number of lines": "https://www.youtube.com/watch?v=bk-w8pK_yrI&list=PL44Kg_kF9XpNZrsNO3zBze6_tjGwzno8Y&index=5",
    "🏆 Leetcode - 150+ DSA Questions":"https://leetcode.com/spurnendu1482000/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = image_url




# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic,caption='Smile a day keeps doctor away' ,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
    """
- ✔️ Internship at SymphonyAI
- ✔️ Teaching Assitant in IIT Madras for C programming
- ✔️ Strong hands on experience and knowledge in Python and DSA
- ✔️ B.S. IIT Madras (2020-2024)
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming:       Master in Python, Intermediate in C, SQL, Java, JavaScript
- 📊 Data Visulization: Matlibplot, Seaborn, 
- 📚 Modeling:          Logistic, linear regression, Decition trees, ANNs, CNNs, RNNs, LLMs
- 🗄️ Databases:         Postgresql
- 🖥️ DSA:               Proficient in Data Structures and Algorithms 
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    # st.write(f"[{project}]({link})")
    st.markdown(f'<p style="margin-left: 30px;"> <a href="{link}" target="_blank">{project}</a></p>', unsafe_allow_html=True)

