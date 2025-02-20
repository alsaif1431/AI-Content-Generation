from content_generation.utils import Azureclient


class ReportGenerator:
    def __init__(self):
        self.template = """
        You are an expert Report writer who will write detailed 
        report for the topic given by the user.
        Always be Precise and Concise to the answer.
        Remember that your sole purpose is to write an Detailed reports.

        If asked for your name, always say "Ai Report writer."

        If the user greets you, just greet them normally.

        If the user tells you something and asks a question on the same, 
        you will answer them correctly.

        Remeber that Report should be a minimum of 1000 words.

        Always include the source of the answer at the end of the report.
        """

        self.conversation_history = []
        self.conversation_history.append({"role": "system", "content": self.template})

    def add_message_to_conversation(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, question):
        self.add_message_to_conversation("user", question)

        response = Azureclient.chat.completions.create(
            model="gpt-4o",
            messages=self.conversation_history,
            max_tokens=1024,
            temperature=0,
        )
        ai_response = response.choices[0].message.content
        self.add_message_to_conversation("assistant", ai_response)
        return ai_response

reportgenerator = ReportGenerator()




