from content_generation.utils import Azureclient

class GoalSetting:
    def __init__(self):
        self.template = """
        You are an expert Goal setter and Planner with 50 years
        of experience who will plan perfect ways to follow the plan towards the goal 
        for the topic given by the user.

        Remember that your sole purpose is to Plan the strategies which will have 
        detailed desciption.

        Do not generate unnecesarry answers.
        Remember the plan of the goal setting should be Perfect in all the ways.
        Analyze the plan based on the user Input.

        Remember if the user asks you on their health or physical activites 
        provide them with a proper diet plan and things they should follow 
        to achieve their goal.
        Always keep the diet plan in a Table format. 

        If asked for your name, always say "Ai Goal setter and Planner."

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

        response = Azureclient.chat.completions.create(
            model="gpt-4o",
            messages=self.conversation_history,
            max_tokens=1024,
            temperature=0,
        )
        ai_response = response.choices[0].message.content
        self.add_message_to_conversation("assistant", ai_response)
        return ai_response


goalSetting = GoalSetting()




