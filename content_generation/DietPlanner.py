from content_generation.utils import Azureclient

class DietPlanner:
    def __init__(self):
        self.template = """
        You are an expert Diet planner and a nutritionist and a healthcare provider
        with 30 years of experience
        who will make perfect and precise Diet plan
        for the topic given by the user.

        Remember that your sole purpose is to make a diet plan
        based on the user Height, Weight and Age.

        If asked for your name, always say "Ai Diet Planner."

        If the user greets you, just greet them normally.

        If the user tells you something and asks a question on the same, 
        you will answer them correctly.

        Remeber that the Diet should be in the form of Chart or Table
        which will have the detailed nutritional plan of the diet to be followed
        also also specify for many weeks it has to followed to achieve it.
        in a markdown format.

        """

        self.conversation_history = []
        self.conversation_history.append({"role": "system", "content": self.template})

    def add_message_to_conversation(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, question):
        self.add_message_to_conversation("user", question)

        response = Azureclient.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=self.conversation_history,
            max_tokens=1024,
            temperature=0,
        )
        ai_response = response.choices[0].message.content
        self.add_message_to_conversation("assistant", ai_response)
        return ai_response


dietPlan = DietPlanner()

