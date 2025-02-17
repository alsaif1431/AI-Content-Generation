import openai
from dotenv import load_dotenv,find_dotenv
import streamlit as st
import os
from content_generation.pdfGenerator import generate_pdf_report

load_dotenv()


class PodcastScript:
    def __init__(self):
        self.template = """
        You are an expert Podcast script writer
        who will write beautiful and meaningful
        podcasts scripts for the topic given by the user.

        Remember that your sole purpose is to write an Podcasts scripts.

        If asked for your name, always say "Ai Podcast script writer."

        If the user greets you, just greet them normally.

        If the user tells you something and asks a question on the same, 
        you will answer them correctly.

        Remember that podcast is done with two or more people on a specific topic.
        The script should have minimum 2000 words.


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
            temperature=0,
        )
        ai_response = response['choices'][0]['message']['content']
        self.add_message_to_conversation("assistant", ai_response)
        return ai_response


scriptWriter = PodcastScript()



