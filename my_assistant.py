# my_assistant.py
# Author: Breanna Ramirez

HANDOFF_WORDS = ["refund", "cancel", "complaint"]


class FlowerAssistant:
    """A rule-based FAQ assistant for a fictional flower shop."""

    def __init__(self, name, faq_tool):
        """Store the assistant's name, FAQ tool, and conversation history."""
        self.name = name
        self.faq_tool = faq_tool
        self.history = []

    def respond(self, user_message):
        """Record the conversation and return a response."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a response based on keywords in the message."""
        text = user_message.lower()

        if self.needs_human(text):
            return "I can't handle that request. I'll refer you to a staff member."

        if any(word in text for word in ["hours", "delivery", "pickup"]):
            return self.faq_reply(user_message)

        if "hello" in text or "hi" in text.split():
            return (
                f"Hello! I'm {self.name}. "
                "I can answer questions about our hours, delivery, and pickup."
            )
        if "faq" in text or "question" in text:
            return self.faq_reply(user_message)

        return "I'm not sure how to help with that. I can answer store FAQs."

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
