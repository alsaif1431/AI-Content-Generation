import openai
from dotenv import load_dotenv,find_dotenv
import streamlit as st
import os
from content_generation.pdfGenerator import generate_pdf_report
from dotenv import load_dotenv,find_dotenv


load_dotenv()




class QuizGenerator:
    def __init__(self):
        self.template = """
        You are an expert Quiz maker who will make the quizzes 
        for the topic given by the user.
        Remember that your sole purpose is to write an Quiz questions.

        If asked for your name, always say "Ai Quiz master."

        If the user greets you, just greet them normally.

        If the user tells you something and asks a question on the same, 
        you will answer them correctly.

        Remeber that quiz should be a in the form Multiple choice questions
        in a markdown format.

        Do add the answers for the questions at the last just like
        [Question Number:Option Number of the answer]
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


quizGen = QuizGenerator()


