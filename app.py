from pathlib import Path

import streamlit as st
from PIL import Image

current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=current_dir / "styles" / "main.css"
resume_file=current_dir / "assets"/ "Nithin_resume.pdf"
profile_pic=current_dir / "assets"/ "profile-pic.png"

PAGE_TITLE = "Portfolio | Nithin Yadav Pandugayala"
PAGE_ICON = "random"
NAME = "Nithin Yadav Pandugayala"
DESCRIPTION = """
DevOps Engineer, Data Science and Machine Learning Enthusiast.
Automation tester using Java and Selenium.
"""
EMAIL = "nithinvasudevyadav0010@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "Currently not available.",
    "LinkedIn": "https://www.linkedin.com/in/nithin-yadav-pandugayala-2a4b2a166/",
    "GitHub": "https://github.com/Budeestar",
    "Twitter": "Currently not available",
}
PROJECTS = {
    "Covid 19 time series analysis: Predicting cases from past data" :"https://github.com/Budeestar/covidpred",
    "Customer Market Segmentation using KMeans: Clustering customers with KMeans":"https://github.com/Budeestar/customer-market",
    "Image data Augmentation with Keras: Enhancing dataset for accuracy.":"https://github.com/Budeestar/data-augmentation",
    "Object detection using YOLOV4: Detecting objects in video image datasets.":"https://github.com/Budeestar/yolov4",
    "Generative Adversarial Networks: Generating fake images to increase dataset accuracy.":"https://github.com/Budeestar/GAN",

}

PUBLICATION={
    "Reconstruction of an Auto-Rickshaw Frontal Crash using FE Simulation with Validation using Captured Crash Video from India":"http://doi.org/10.4271/2021-28-0257",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#st.title("NV's page")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=280)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE  ---
st.write('\n')
st.subheader("PROFESSIONAL EXPERIENCE")

st.write('\n')
st.write("""
Cognizant Technology Solutions, Hyderabad, India

Programmer Analyst | 2021 – 2023
"""
         )
st.write(
    """
-	Debugged and troubleshooted software, performed comprehensive system analysis, which increased the software efficiency from 35% to 85%
-	delivered effective solutions that optimized business processes and drove seamless user experiences. 
-	Created Azure pipelines triggered hourly for frameworks where the average success rate is more than 70%
-	Scripted a framework for automation using reusable functions that was adopted by 8 other teams 
-	Implemented a shell adapter for Java-Maven framework authentication which helped to complete 11 other automation flows
-	Contributed to a conference demonstrating Automation flow with Computer Vision which helps for blind people as 1% of the world is visually impaired.
-	Successfully revived 1 year-long halted Automation flow using Computer Vision and OCR techniques and cut down manual work by entire 100%
-	Engineered a cutting-edge container hosting solution leveraging Java and Node.js, introducing a game-changing API call, and optimizing body and headers; achieved an impressive 95% increase in hosting capabilities
-	Live logging in containerized frameworks was created for every 30 seconds.
-	Supported many teams during their onboarding and raised the success rate of the script to almost 100%
-	Employed XML scripts to call Python Flask API using Java for OTP responses which helped to complete 7 automation flows.

"""
)

#--- publication ---
st.write('\n')
st.subheader("Publication")
for publication,link in PUBLICATION.items():
    st.write(f"[{publication}]({link})")

st.subheader("Used technologies and Softwares")
st.write("""
| Python, OpenCV, MATLAB, Video Stitching, Ansys, LS-Dyna
""")
st.write('\n')
st.write("""
-	Conducted frontal crash simulation using three-wheeler CAE model and a driver dummy.
-	Compared frontal crash effects with Simulation and real-time crash video.
-	Stitched frames to calculate PPM (Pixels per meter) for velocity estimation.
-	Accurate analysis aiding manufacturers in crash simulations.
-	Cost-effective alternative to real car crash analysis.

""")

st.write('\n')
st.subheader("EDUCATION: Graduate")
st.write("""
University at Buffalo, Buffalo, New York
Master’s degree | 2023- 2025
""")
st.write('\n')
st.subheader("EDUCATION: Under-Graduate")
st.write("""
Sastra University, Thanjavur, India
Bachelor of Technology | 2021
""")

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write("""
-   Programming/Scripting Languages: Python, Java, C++, C, JavaScript, Shell scripting.
-   Operating Systems: Windows, Linux (Ubuntu, Debian).
-   Skills and Tools: Git, MATLAB, AzureDevOps, Docker, Kubernetes, TensorFlow, Keras, Heroku, Machine learning, Deep learning, Data science
-   Databases: MySQL, Oracle, MongoDB

""")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("\n")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Certifications")
st.write("""
-   Microsoft Azure AZ-104
-   Coursera Deep Learning Specialization
-   Coursera Excel Specialization
""")


st.write('\n')
st.subheader("Awards")
st.write("\n")
st.write("""
-	Finalist in Brakes India Industrial Hackathon on Machine Vision
-	Finalist in the WACAMLDS Australian Hackathon 

""")
