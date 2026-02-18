from datetime import datetime, timezone
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from models.state_models import InventoryState, MongoQuery

model = GoogleGenerativeAI(model="gemini-2.5-flash")


def products_handler(state: InventoryState) -> InventoryState:
    """Build a MongoDB query for the Product collection"""
    
    user_query = state["user_query"]
    owner_id = state["owner_id"]

    today = datetime.now(timezone.utc).date()
    end_of_yesterday = datetime.combine(today, datetime.min.time(), tzinfo=timezone.utc)

    parser = PydanticOutputParser(pydantic_object=MongoQuery)
    format_instructions = parser.get_format_instructions()

    prompt = f"""
You are a MongoDB query generator for a shop inventory assistant.

Today's date (ISO 8601, UTC) is: "{end_of_yesterday}".

You ONLY handle queries related to the Products collection.

Product collection ("products") schema:
- owner: String (shop owner id/email, REQUIRED)
- name: String (product name)
- category: String
- actualPrice: Number (cost price)
- sellingPrice: Number (selling price)
- quantity: Number (current stock)
- reorderLevel: Number (low-stock threshold)
- supplier: String
- expirationDate: Date
- dateAdded: Date
- dateUpdated: Date

Your job:
- Every filter MUST include: {{ "owner": "{owner_id}" }}
- Create ONE MongoDB find filter that can be used as Product.find(filter).
- Use ONLY these field names in the filter.
- You may use $gt, $lt, $gte, $lte, $and, $or, and $regex where needed.
- For "expired" products, use: {{ "expirationDate": {{ "$lt": "{end_of_yesterday}" }} }}
- DO NOT include sort/limit/projection; only the filter object.

Return the result using this JSON schema:
{format_instructions}

User message:
{user_query}
"""

    raw_msg = model.invoke(prompt)
    raw_text = raw_msg.content if hasattr(raw_msg, "content") else str(raw_msg)
    mongo_query: MongoQuery = parser.parse(raw_text)
    
    filter_obj = mongo_query.filter
    filter_obj["owner"] = owner_id

    if "expire" in user_query.lower():
        filter_obj["expirationDate"] = {"$lt": end_of_yesterday}

    return {"mongo_query": filter_obj, "collection": "products"}