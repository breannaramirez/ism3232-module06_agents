from my_assistant import FlowerAssistant
from my_tool import FAQLookup


def make_assistant():
    """Create a fresh flower shop assistant for each test."""
    faqs = {
        "hours": "We are open Monday through Saturday, 9 AM to 6 PM.",
        "delivery": "We offer local delivery Monday through Saturday.",
        "pickup": "You can pick up orders during store hours.",
    }
    faq_tool = FAQLookup(faqs)
    return FlowerAssistant("Flora", faq_tool)


def test_faq_tool_finds_known_topic():
    tool = FAQLookup({"hours": "9 AM to 6 PM"})
    assert tool.find_topic("What are your hours?") == "hours"


def test_faq_question_uses_tool():
    assistant = make_assistant()
    reply = assistant.respond("Do you offer delivery?")
    assert reply == "We offer local delivery Monday through Saturday."


def test_missing_topic_gets_helpful_reply():
    assistant = make_assistant()
    reply = assistant.respond("I have a question about flowers")
    assert "Which topic?" in reply


def test_refund_request_goes_to_staff():
    assistant = make_assistant()
    reply = assistant.respond("Can I get a refund?")
    assert "staff member" in reply


def test_unknown_request_gets_safe_reply():
    assistant = make_assistant()
    reply = assistant.respond("Do you sell balloons?")
    assert "not sure" in reply


def test_conversation_history():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What are your hours?")
    assert len(assistant.history) == 4
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"


def test_cancellation_request_goes_to_staff():
    assistant = make_assistant()
    reply = assistant.respond("I want to cancel my order")
    assert "staff member" in reply
