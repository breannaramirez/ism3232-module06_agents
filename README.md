# Lab 10: OOP for Agents

## Mini-Project: Bloom & Co. FAQ Assistant

For my mini-project, I created Flora, an FAQ assistant for a fictional flower shop called Bloom & Co. The assistant uses a separate FAQ lookup tool to answer customer questions about store hours, delivery and pickup. It is a mock assistant because the store information is made up and the responses are based on keyword rules rather than a real AI model. Requests involving refunds, cancellations or complaints are referred to a staff member because those situations may require access to customer orders or additional assistance. If the assistant used real customer data, a potential risk would be exposing private information if the data was not handled securely.

## Week 11 - Adding a Local Model

I updated my Bloom & Co. assistant, Flora, to use Ollama for questions that aren't handled by the FAQ tool or handoff rules. The model correctly answered that the shop is located at 25 Garden Lane and that we sell fresh flowers, bouquets, and floral arrangements. However, when I asked about wedding planning, it said we don't offer that service even though I hadn't provided that information. This showed me that the model can still make assumptions instead of admitting it doesn't know. I kept store hours, delivery, and pickup in the FAQ tool, and refund and complaint requests in code because those responses need to be reliable.