# my_main.py
# Author: Breanna Ramirez

from my_assistant import FlowerAssistant
from my_tool import FAQLookup

FAQS = {
    "hours": "We are opne Monday through Saturday, 9 AM to 6 PM.",
    "delivery": "We offer loal delivery Monday through Saturday.",
    "pickup": "You can pick up orders during store hours.",
}

faq_tool = FAQLookup(FAQS)
flora = FlowerAssistant("Flora", faq_tool)

print("Welcome to Bloom & Co.!")
print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message.lower() != "quit":
    print(f"{flora.name}: {flora.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(flora.history)}")
