from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "ArpanMishra_Resume.pdf"
profile_pic = current_dir / "assets" / "my-profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Arpan Mishra"
PAGE_ICON = ":wave:"
NAME = "Arpan Mishra"
DESCRIPTION = """
Enthusiastic SDET eager to contribute to team success through hard work, attention to detail and excellent organizational skills.
"""
EMAIL = "arpanmishra63@gmail.com"
SOCIAL_MEDIA = {
    # "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "linkedin.com/in/arpan-mishra",
    # "GitHub": "https://github.com",
    # "Twitter": "https://twitter.com",
}
PROJECTS = [
    "🏆 UI Automation - Identification of the UI test cases and automation using Cypress Framework.",
    "🏆 API Automation - Identification of the API test cases and automation using Pytest Framework.",
    "🏆 API Automation Framework setup and enhancements to reduce overall execution time.",
    "🏆 Dashbord setup using python library named streamlit - Created accurate and efficient test scripts to manage automated testing for Android using Appium.",
    "🏆 ELK setup to present the difference quality matrix - Created accurate and efficient test scripts to manage automated testing for Android using Appium.",
    "🏆 API Automation Framework setup and enhancements to reduce overall execution time - Created accurate and efficient test scripts to manage automated testing for Android using Appium.",
    "🏆 Android Automation of Recharges & Utilities - Created accurate and efficient test scripts to manage automated testing for Android using Appium.",
    "🏆 IOS Automation of Recharges & Utilities - Created accurate and efficient test scripts to manage automated testing for IOS using XCUITest.",
]

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

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


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 5 Years experience as a strong full stack SDET 
- ✔️ Strong hands on experience and knowledge in Cypress and Python
- ✔️ Good understanding of WEB, Mobile and Api Automation
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Strong knowledge of Rest API and SQL
- ✔️ Strong knowledge of Rest API and SQL
- ✔️ Good understanding of Performance testing using JMeter
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming Languages: Expertise in programming languages such as Python (Pyest, Pandas), Java, Javascript, SQL
- 👩‍💻 Testing Methodologies: Strong knowledge of various testing methodologies, including unit testing, integration testing, regression testing, and performance testing.
- 👩‍💻 Test Management Tools: Experience using test management tools like Jira, TestRail, or Quality Center for test planning, execution, and defect tracking.
- 👩‍💻 Continuous Integration/Continuous Deployment (CI/CD): Familiarity with CI/CD pipelines and tools like Jenkins, GitLab CI/CD, or Travis CI to automate build, test, and deployment processes.
- 👩‍💻 Test Automation: Proficiency in developing and maintaining automated test frameworks using tools such as Cypress, Pytest or Appium.
- 👩‍💻 Version Control Systems: Proficient in using Git or SVN for version control and collaboration with other team members.
- 📊 Data Visualization: Elastic, Streamlit
- 📚 Performance Testing: Jmeter
- 🗄️ Databases: Experience with SQL queries and database testing using tools like MS SQL Server
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Soft Skills")
st.write(
    """
- 👩‍ Analytical Thinking: Strong analytical and problem-solving skills to identify, troubleshoot, and debug software issues.
- 👩‍ Attention to Detail: Keen attention to detail to ensure comprehensive test coverage and identify potential issues or gaps.
- 👩‍ Collaboration: Ability to work effectively within cross-functional teams, collaborating with developers, QA engineers, and product managers to ensure quality throughout the software development lifecycle.
- 👩‍ Communication: Excellent written and verbal communication skills to articulate complex technical concepts, report bugs effectively, and provide clear and concise documentation.
- 👩‍ Adaptability: Flexibility to adapt to changing priorities, project requirements, and new technologies in a fast-paced and dynamic environment.
- 👩‍ Time Management: Strong organizational and time management skills to prioritize tasks, meet deadlines, and deliver high-quality results.
- 👩‍ Continuous Learning: Proactive attitude towards learning and staying updated with the latest industry trends, technologies, and testing practices.
"""
)



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Member Technical | D. E. Shaw India Pvt. Ltd.**")
st.write("06/2022 - Present")
st.write(
    """
- ► API Automation Framework setup and enhancements to reduce overall execution time.
- ► Leading the team to 2 members to complete the automation goals and reduce the turn around time by 70%
- ► ELK setup to present the difference quality matrix
- ► Dashboard setup using python library named streamlit
- ► UI and API framework optimization
- ► Performance Suite setup using Jmeter
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Member Technical | D. E. Shaw India Pvt. Ltd.**")
st.write("06/2020 - 06/2022")
st.write(
    """
- ► Identification of the UI test cases and automating the same using Cypress Framework.
- ► Identification of the API test cases and automation using Pytest Framework.
- ► Coordination with the members of the test team and the development team to solve the issues.
- ► Performance testing and analysis of the different API using Jmeter.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**QA Engineer | PAYTM (ONE97 Communications Limited)**")
st.write("09/2018 - 06/2020")
st.write(
    """
- ► Selection or identification of test cases for automation from existing test case documentation.
- ► Find solutions for issues related to object identity issues and error handling.
- ► Test, build, design, deployment, and ability to maintain continuous integration and continuous delivery process using tools like Jenkins, maven Git, etc.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project in PROJECTS:
    st.write(f"{project}")



# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("🚧", "**B.Tech in Computer Science | Ajay Kumar Garg Engineering College**")
st.write("07/2014 - 06/2018")


# --- HOBBIES & INTERESTS ---
st.write('\n')
st.subheader("Hobbies and Interests")
st.write(
    """
- ► Fitness
- ► Listening to Music
- ► Playing Cricket
- ► Reading
"""
)

