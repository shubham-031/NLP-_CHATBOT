from typing import TypedDict, Literal, Optional, Dict, Any, Annotated, List
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages


class IntentExtractor(BaseModel):
    intent: Literal["products", "suppliers", "bills", "analytics", "customers", "chitchat"] = Field(
        ...,
        description=(
            "High-level inventory intent for the query: "
            "'products' (product info/stock), "
            "'suppliers' (vendor-related), "
            "'bills' (invoices), "
            "'customers' (customer info), "
            "'analytics' (sales/profit insights), "
            "'chitchat' (greetings/previous conversations)"
        ),
    )


class MongoQuery(BaseModel):
    filter: Dict[str, Any] = Field(
        ...,
        description="MongoDB filter for the collection, using fields from the schema.",
    )


class InventoryState(TypedDict):
    owner_id: str
    user_query: str
    mongo_query: Optional[Dict[str, Any]]
    intent: Literal["products", "suppliers", "bills", "customers", "analytics", "chitchat"]
    collection: Optional[str]
    db_results: Dict[str, Any]
    response: Optional[str]
    messages: Annotated[List[BaseMessage], add_messages]