# my_main.py
# Author: Breanna Ramirez

from my_assistant import FlowerAssistant
from my_tool import FAQLookup
from ollama_model import OllamaModel

FAQS = {
    "hours": "We are open Monday through Saturday, 9 AM to 6 PM.",
    "delivery": "We offer local delivery Monday through Saturday.",
    "pickup": "You can pick up orders during store hours.",
}

INSTRUCTIONS = """You are Flora, a friendly support assistant for Bloom & Co., a flower shop.
Answer in one short sentence.
Our shop is located at 25 Garden Lane.
We sell fresh flowers, bouquets, and floral arrangements.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to refer the customer to a staff member."""

faq_tool = FAQLookup(FAQS)
model = OllamaModel("granite4.1:3b")

flora = FlowerAssistant("Flora", faq_tool, model, INSTRUCTIONS)

print("Welcome to Bloom & Co.!")
print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message.lower() != "quit":
    print(f"{flora.name}: {flora.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(flora.history)}")
