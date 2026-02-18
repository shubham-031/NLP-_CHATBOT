from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from models.state_models import InventoryState, IntentExtractor

model = GoogleGenerativeAI(model="gemini-2.5-flash")


def supervisor_router(state: InventoryState) -> InventoryState:
    """Router node: detects high-level intent from user_query"""
    
    user_query = state["user_query"]
    summary = state.get("response", "")
    db_results = state.get("db_results", "")

    parser = PydanticOutputParser(pydantic_object=IntentExtractor)
    format_instructions = parser.get_format_instructions()

    prompt = f"""
You are an intent classifier for a small shop inventory assistant.

Your job:
- Read the user's message.
- Choose exactly ONE intent from this list:
  - "products"   : product details, stock, price, barcode, item info.
  - "suppliers"  : vendors, purchase orders, supplier balances or payments.
  - "bills"      : sales bills, invoices, receipts, order history.
  - "customers"  : customers, phone numbers, loyalty, credit/udhari.
  - "analytics"  : sales summary, revenue, profit, margin, trends, top/bottom items.
  - "chitchat"   : greetings or previous information related message if present {summary}, and db_results if present {db_results}

Rules:
- Always return exactly one of these words as the value of "intent".
- If you are not sure, pick the closest matching intent.

Return the result using this JSON schema:
{format_instructions}

User message:
{user_query}
"""

    raw_msg = model.invoke(prompt)
    raw_text = raw_msg.content if hasattr(raw_msg, "content") else str(raw_msg)
    intent_obj: IntentExtractor = parser.parse(raw_text)

    return {"intent": intent_obj.intent}