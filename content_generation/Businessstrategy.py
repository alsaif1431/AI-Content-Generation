import openai
import streamlit as st
from content_generation.pdfGenerator import generate_pdf_report
from dotenv import load_dotenv,find_dotenv
import os
load_dotenv()




class BusinessStrategy:
    def __init__(self):
        self.template = """
        You are an expert Business Strategy Planner with 50 years
        of experience as a Entrepreneur who will plan strategies 
        for the topic given by the user.

        Remember that your sole purpose is to Plan the strategies which will have 
        detailed desciption of the Plan with proof and possible outcomes.

        Do not generate unnecesarry answers.

        If asked for your name, always say "Ai Business strategy Planner."

        If the user greets you, just greet them normally.

        If the user tells you something and asks a question on the same, 
        you will answer them correctly.

        
        """

        self.conversation_history = []
        self.conversation_history.append({"role": "system", "content": self.template})

    def add_message_to_conversation(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, question):
        self.add_message_to_conversation("user", question)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=self.conversation_history,
            max_tokens=1024,
            temperature=0,
        )
        ai_response = response['choices'][0]['message']['content']
        self.add_message_to_conversation("assistant", ai_response)
        return ai_response


bussiness = BusinessStrategy()



