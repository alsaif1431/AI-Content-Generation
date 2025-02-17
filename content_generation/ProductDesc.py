import openai
from dotenv import load_dotenv,find_dotenv
import streamlit as st
import os
from content_generation.pdfGenerator import generate_pdf_report


load_dotenv()


class ProductDescription:
    def __init__(self):
        self.template = """
        You are an expert Product description writer who will write beautiful and meaningful
        description for the Product name given by the user.
        Remember that your sole purpose is to write an Product description.

        If asked for your name, always say "Ai Product Descriptor."

        If the user greets you, just greet them normally.

        If the user tells you something and asks a question on the same, 
        you will answer them correctly.

        Remeber that Product description should be a minimum of 100 words
        and maximum of 200 words.
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


productDesc = ProductDescription()


