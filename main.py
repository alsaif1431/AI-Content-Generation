import streamlit as st
from content_generation.BlogsArticles import articlewriter 
from content_generation.DietPlanner import dietPlan 
from content_generation.pdfGenerator import generate_pdf_report 
from content_generation.Businessstrategy import bussiness
from content_generation.GoalSettingandPlanning import goalSetting 
from content_generation.PodcastsScripts import scriptWriter
from content_generation.Quizzes import quizGen
from content_generation.Reports import reportgenerator
from content_generation.ProductDesc import productDesc 
from PIL import Image

# -------------------------------
# Page Configuration (Updated)
# -------------------------------
st.set_page_config(
    page_title="GenAI Content Generator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.sidebar.markdown(
    """
    <div style="background-color: #f2f2f2; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="text-align: center; color: #333;">GenAI Content Hub</h2>
        <p style="text-align: center; font-size: 14px; color: #555;">
            Your one-stop destination for creating diverse, engaging content powered by AI.
        </p>
    </div>
    <div style="background-color: #fff; padding: 15px; border-radius: 10px;">
        <h4 style="color: #333;">Features</h4>
        <ul style="font-size: 14px; color: #555; line-height: 1.6;">
            <li>Engaging Blogs & Articles</li>
            <li>Compelling Business Strategies</li>
            <li>Personalized Diet & Goal Planning</li>
            <li>Creative Podcast Scripts</li>
            <li>Detailed Product Descriptions</li>
            <li>Fun and Informative Quizzes</li>
            <li>Dynamic Reports</li>
        </ul>
        <hr style="border-top: 1px solid #ccc;">
        <h4 style="color: #333;">Connect</h4>
        <p style="font-size: 12px; color: #777;">
            Follow me on our social channels for updates and tips.
        </p>
        <p style="text-align: center;">
            <a href="https://www.linkedin.com/in/saif-pasha-59643b197/" target="_blank" style="margin-right: 10px;">LinkedIn</a>
            <a href="https://github.com/alsaif1431" target="_blank">Github</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Optionally, you can also add a logo or image:
# logo = Image.open("logo.png")
# st.sidebar.image(logo, use_column_width=True)
# -------------------------------
# App Header & Introduction
# -------------------------------
st.title("Welcome to the AI-Powered Content Generation Hub 🎥")
st.markdown(
    """
    <span style='color:green; font-weight:bold;'>
        ✅ Powered by Groq 's <a href='https://console.groq.com' target='_blank'>Llama 3.3 model</a>!
    </span>
    """,
    unsafe_allow_html=True
)
st.write(
    "This platform is your go-to destination for generating diverse content such as articles, blogs, podcasts, scripts, product descriptions, and more!"
)

st.header("What can you do here?")
st.markdown(
    """
    - **Article and Blog Writing:** Craft engaging articles on various topics.
    - **Podcast Scripting:** Write scripts for podcasts or audio content.
    - **Report Generation:** Create detailed reports tailored to your needs.
    - **Diet Planning:** Get personalized diet plans.
    - **Goal Setting and Planning:** Plan and achieve your goals.
    - **Business Strategies:** Develop effective business strategies.
    - **Product Description:** Generate detailed product descriptions.
    - **Quizzes:** Create fun and informative quizzes.
    """
)

st.header("Let's dive into your selection of the topic")
optionSelected = st.selectbox(
    "What kind of content would you like to generate?",
    (
        "Blogs and Articles",
        "Business Strategies",
        "Diet Planning",
        "Goal setting",
        "Podcasts scripts",
        "Product Description",
        "Quizzes",
        "Reports",
    ),
    placeholder="Select your topic below",
)

# -------------------------------
# Content Generation Options
# -------------------------------
if optionSelected == "Blogs and Articles":
    st.header("Blogs and Articles Writer ✍️")
    question = st.text_input("Enter the Title", "Generative AI")
    option = st.selectbox(
        "Select your language", ("English", "Kannada", "French", "Hindi")
    )
    if st.button("Generate"):
        with st.spinner("Thinking..."):
            response = articlewriter.get_response(question, option)
            st.write(response)
            pdf_report = generate_pdf_report(response)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="Blog_article.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Business Strategies":
    st.header("Business Strategy Planner 💼")
    question = st.text_input("Enter the product to plan a business strategy", "Wrist watches")
    if st.button("Plan strategy"):
        with st.spinner("Planning..."):
            response = bussiness.get_response(question)
            st.write(response)
            pdf_report = generate_pdf_report(response)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="BusinessStrategy.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Diet Planning":
    st.header("Personal Diet Planner 🍽️")
    question = st.text_input(
        "Please enter your details (Height, Weight, Age, etc.)",
        "I need to gain weight, age 22, Height 5'11, Weight 50. Please plan a diet for me."
    )
    if st.button("Plan Diet"):
        with st.spinner("Planning diet..."):
            response = dietPlan.get_response(question)
            st.write(response)
            pdf_report = generate_pdf_report(response)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="DietPlan.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Goal setting":
    st.header("Goal Setting and Planning 🎯")
    question = st.text_input("Enter your goal", "To start my own clothing brand")
    if st.button("Plan goal"):
        with st.spinner("Planning..."):
            response = goalSetting.get_response(question)
            st.write(response)
            pdf_report = generate_pdf_report(response)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="GoalPlanner.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Podcasts scripts":
    st.header("Podcasts Scripts 🎙️")
    question = st.text_input("Enter the Podcast title", "Gen AI vs Traditional AI for 2 people")
    if st.button("Generate script"):
        with st.spinner("Processing..."):
            response = scriptWriter.get_response(question)
            st.write(response)
            pdf_report = generate_pdf_report(response)
            st.download_button(
                label="Download Script as PDF",
                data=pdf_report,
                file_name="PodcastScript.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Product Description":
    st.header("Product Description 📦")
    question = st.text_input("Enter the product title", "Samsung S20")
    if st.button("Generate Description"):
        with st.spinner("Describing..."):
            response = productDesc.get_response(question)
            st.write(response)
            pdf_report = generate_pdf_report(response)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="ProductDesc.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Quizzes":
    st.header("Quiz Generator 🧩")
    question = st.text_input("Enter the Quiz Title", "Python")
    if st.button("Generate"):
        with st.spinner("Thinking..."):
            response = quizGen.get_response(question)
            st.write(response)
            pdf_report = generate_pdf_report(response)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="Quizzes.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Reports":
    st.header("Report Generator 📝")
    question = st.text_input("Enter the Report title", "Artificial Intelligence")
    if st.button("Generate Report"):
        with st.spinner("Generating..."):
            response = reportgenerator.get_response(question)
            st.markdown(response)
            pdf_report = generate_pdf_report(response)
            st.download_button(
                label="Download Report as PDF",
                data=pdf_report,
                file_name="Report.pdf",
                mime="application/pdf",
            )
else:
    st.info("Please select an option from the dropdown above.")

# -------------------------------
# Footer (Updated)
# -------------------------------
footer_html = """
<div style="text-align: center; margin: 10px;">
    <p>
        © 2024. All rights reserved. | 
        <a href="https://www.linkedin.com/in/saif-pasha-59643b197/" target="_blank">LinkedIn</a> |
        <a href="https://github.com/alsaif1431" target="_blank">Github</a>
    </p>
</div>
"""

footer_css = """
<style>
.footer {
    position: fixed;
    z-index: 1000;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    color: #333;
    text-align: center;
    padding: 10px 0;
}
</style>
"""

footer = f"{footer_css}<div class='footer'>{footer_html}</div>"
st.markdown(footer, unsafe_allow_html=True)

