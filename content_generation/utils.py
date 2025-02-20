import os
import streamlit as st
from groq import Groq
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv(override=True)


# Azureclient = AzureOpenAI(
#     api_key=st.secrets.get("AZURE_API_KEY"),
#     api_version=st.secrets.get("AZURE_API_VERSION"),
#     azure_deployment=st.secrets.get("AZURE_DEPLOYMENT_MODEL"),
#     azure_endpoint=st.secrets.get("AZURE_ENDPOINT"),
# )

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
Azureclient = Groq(api_key=GROQ_API_KEY)
