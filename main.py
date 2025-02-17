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


favicon = Image.open("favicon.png")
st.set_page_config(
        page_title="GenAI Demo | Trigent AXLR8 Labs",
        page_icon=favicon,
        layout="wide",
        initial_sidebar_state="expanded"
    )

api_key = st.secrets["OPENAI_API_KEY"]
if api_key is None:
        raise ValueError(
            "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")


# Sidebar Logo
logo_html = """
<style>
    [data-testid="stSidebarNav"] {
        background-image: url(https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png);
        background-repeat: no-repeat;
        background-position: 20px 20px;
        background-size: 80%;
    }
</style>
"""
st.sidebar.markdown(logo_html, unsafe_allow_html=True)

st.title("Welcome to Ai-Powered Content Generation Hub 🎥")

if api_key:
        success_message_html = """
        <span style='color:green; font-weight:bold;'>✅ Powering the Chatbot using Open AI's 
        <a href='https://platform.openai.com/docs/models/gpt-3-5' target='_blank'>gpt-3.5-turbo-0613 model</a>!</span>
        """

        # Display the success message with the link
        st.markdown(success_message_html, unsafe_allow_html=True)
        openai_api_key = api_key
else:
    openai_api_key = st.text_input(
        'Enter your OPENAI_API_KEY: ', type='password')
    if not openai_api_key:
        st.warning('Please, enter your OPENAI_API_KEY', icon='⚠️')
        stop = True
    else:
        st.success('Get ready for some content generation!', icon='👉')
st.write(
    "This platform is your go-to destination for generating diverse content across articles, blogs, podcasts, scripts, and product descriptions!"
)

st.header("What can you do here?")
st.markdown(
    """
    - **Article and Blogs Writing:** Craft engaging articles on various topics in dfferent languages.
    - **Podcast Scripting:** Write scripts for podcasts or audio content.
    - **Reports Generation:** Create reports for any requirements based on your requiremments.
    - **Diet Planning:** Plans a proper diet to be followed.
    - **Goal setting and Planning:** Planns and set the required steps to achieve the goal.
    - **Business strategies:**Writes the different business strategies for the products.
    - **Product Decription:** Generats the detailed description for the various products.
    - **Quizzes:** Generats the Quizzes on the topics in a MCQformat.

    This platform empowers you to create high-quality content across different formats and purposes.
    """
)

st.header("Let's dive into your selection of the Topic")

optionSelected = st.selectbox(
    "What kind of stuff you would like to generate?",
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
    index=None,
    placeholder="Select your topic below",
)

if optionSelected == "Blogs and Articles":
    st.header("Blogs and Articles writer ✍️")
    question = st.text_input("Enter the Title", "Generative AI")
    option = st.selectbox(
        "Select your language", ("English", "Kannada", "French", "Hindi")
    )
    if st.button("Generate") and option:
        with st.spinner("Thinking..."):
            response = articlewriter.get_response(question, option)
            forPdf = response
            st.write(response)

            pdf_report = generate_pdf_report(forPdf)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="Blog/article.pdf",
                mime="application/pdf",
            )
elif optionSelected == "Business Strategies":
    st.header("Business Strategy Planner 💼")
    question = st.text_input(
        "Enter the Product to plan a business strategy", "Wrist watches"
    )
    if st.button("Plan strategy"):
        with st.spinner("Planning..."):
            response = bussiness.get_response(question)
            forPdf = response
            st.write(response)

            pdf_report = generate_pdf_report(forPdf)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="BusinessStrategy.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Diet Planning":
    st.header("Personal Diet Planner 🍽️")
    question = st.text_input(
        "Please enter you query with your Height, Weight and Age",
        "I need to gain weight my age is 22, Height 5'11, Weight 50 please plan a diet for me",
    )
    if st.button("Plan Diet"):
        with st.spinner("Planning diet..."):
            response = dietPlan.get_response(question)
            forPdf = response
            st.write(response)

            pdf_report = generate_pdf_report(forPdf)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="Dietplan.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Goal setting":
    st.header("Goal Setting and Planning 🎯")
    question = st.text_input("Enter your goal", "To start my own Brand on clothing")
    if st.button("Plan goal"):
        with st.spinner("Planning..."):
            response = goalSetting.get_response(question)
            forPdf = response
            st.write(response)

            pdf_report = generate_pdf_report(forPdf)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="GoalPlanner.pdf",
                mime="application/pdf",
            )
elif optionSelected == "Podcasts scripts":
    st.header("Podcasts scripts 🎙️")
    question = st.text_input(
        "Enter the Podcast title", "Gen ai vs Traditional Ai for 2 people"
    )
    if st.button("Generate script"):
        with st.spinner("Processing..."):
            response = scriptWriter.get_response(question)
        forPdf = response
        st.write(response)

        pdf_report = generate_pdf_report(forPdf)
        st.download_button(
            label="Download Script as PDF",
            data=pdf_report,
            file_name="PodcastScript.pdf",
            mime="application/pdf",
        )

elif optionSelected == "Product Description":
    st.header("Product Description 📦")
    question = st.text_input("Enter the product title", "Samsung s20")
    if st.button("Generate Description"):
        with st.spinner("Describing..."):
            response = productDesc.get_response(question)
            forPdf = response
            st.write(response)

            pdf_report = generate_pdf_report(forPdf)
            st.download_button(
                label="Download as PDF",
                data=pdf_report,
                file_name="ProductDesc.pdf",
                mime="application/pdf",
            )

elif optionSelected == "Quizzes":
    st.header("Quizz Generator 🧩")
    question = st.text_input("Enter the Quiz Title", "Python")
    if st.button("Generate"):
        with st.spinner("Thinking..."):
            response = quizGen.get_response(question)
            forPdf = response
            st.write(response)

            pdf_report = generate_pdf_report(forPdf)
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
            forPdf = response
            st.markdown(response)

            pdf_report = generate_pdf_report(forPdf)
            st.download_button(
                label="Download Report as PDF",
                data=pdf_report,
                file_name="Report.pdf",
                mime="application/pdf",
            )
else:
    st.info("Please select something")

 # Footer
footer_html = """
<div style="text-align: right; margin-right: 10%;">
    <p>
        Copyright © 2024, Trigent Software, Inc. All rights reserved. | 
        <a href="https://www.facebook.com/TrigentSoftware/" target="_blank">Facebook</a> |
        <a href="https://www.linkedin.com/company/trigent-software/" target="_blank">LinkedIn</a> |
        <a href="https://www.twitter.com/trigentsoftware/" target="_blank">Twitter</a> |
        <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank">YouTube</a>
    </p>
</div>
"""

# Custom CSS to make the footer sticky
footer_css = """
<style>
.footer {
    position: fixed;
    z-index: 1000;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
}
</style>
"""


footer = f"{footer_css}<div class='footer'>{footer_html}</div>"

# Rendering the footer
st.markdown(footer, unsafe_allow_html=True)