import streamlit as st
from groq import Groq
from openai import AzureOpenAI


# Azureclient = AzureOpenAI(
#     api_key=st.secrets.get("AZURE_API_KEY"),
#     api_version=st.secrets.get("AZURE_API_VERSION"),
#     azure_deployment=st.secrets.get("AZURE_DEPLOYMENT_MODEL"),
#     azure_endpoint=st.secrets.get("AZURE_ENDPOINT"),
# )



Azureclient = Groq(api_key="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")
