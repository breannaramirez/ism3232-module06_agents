# my_tool.py
# Author: Breanna Ramirez


class FAQLookup:
    """A tool that stores and looks up answers to common store question."""

    def __init__(self, faqs):
        """Store the FAQ topics and their answers."""
        self.faqs = faqs

    def find_topic(self, text):
        """Find a known FAQ topic mentioned in a message."""
        for topic in self.faqs:
            if topic in text.lower():
                return topic
        return None

    def answer_for(self, topic):
        """Return the answer for a topic, or None if it is unknown."""
        if topic in self.faqs:
            return self.faqs[topic]
        return None
