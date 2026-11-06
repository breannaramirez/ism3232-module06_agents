# my_assistant.py
# Author: Breanna Ramirez

HANDOFF_WORDS = ["refund", "cancel", "complaint"]


class FlowerAssistant:
    """A flower shop assistant that uses rules, an FAQ tool, and a model."""

    def __init__(self, name, faq_tool, model, instructions):
        """Store the assistant's settings, tools, model, and history."""
        self.name = name
        self.faq_tool = faq_tool
        self.model = model
        self.instructions = instructions
        self.history = []

    def respond(self, user_message):
        """Record the conversation and return a response."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Use rules first, then the model for other questions."""
        text = user_message.lower()

        if self.needs_human(text):
            return "I can't handle that request. I'll refer you to a staff member."

        if any(word in text for word in ["hours", "delivery", "pickup"]):
            return self.faq_reply(user_message)

        if "faq" in text or "question" in text:
            return self.faq_reply(user_message)

        return self.model_reply()

    def model_reply(self):
        """Ask the model for a response or give a safe fallback."""
        reply = self.model.reply(self.instructions, self.history)

        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."

        return reply

    def needs_human(self, text):
        """Check whether a request should be handled by staff."""
        return any(word in text for word in HANDOFF_WORDS)

    def faq_reply(self, user_message):
        """Use the FAQ tool to answer a customer's question."""
        topic = self.faq_tool.find_topic(user_message)

        if topic is None:
            return "Which topic? I can help with hours, delivery, or pickup."

        answer = self.faq_tool.answer_for(topic)

        if answer is None:
            return "I couldn't find information about that topic."

        return answer
