"""
Chatbot Runner - Workflow Configuration
Builds and exports the complete LangGraph workflow
"""
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict, Literal, Optional, Dict, Any, List, Annotated
from pydantic import Field
from langgraph.graph import add_messages
from langchain_core.messages import BaseMessage

# Import handlers
from handlers.products_handler import products_handler
from handlers.bills_handler import bills_handler
from handlers.suppliers_handler import suppliers_handler
from handlers.customers_handler import customers_handler
from handlers.supervisor_router import supervisor_router

# Import analytics (fixed import)
from analytics.analytics_tools import (
    analytics_llm_node,
    analytics_formatter_node,
    analytics_tools,
    ToolNode
)

# Import utilities
from utils.helpers import executor_node, response_node, chitchat_node


# ==================== STATE DEFINITION ====================
class InventoryState(TypedDict):
    """State for inventory chatbot"""
    owner_id: str
    user_query: str
    mongo_query: Optional[Dict[str, Any]]
    intent: Optional[Literal["products", "suppliers", "bills", "customers", "analytics", "chitchat"]]
    collection: Optional[str]
    db_results: Optional[Dict[str, Any]]
    response: Optional[str]
    messages: Annotated[List[BaseMessage], add_messages]


# ==================== ROUTING FUNCTIONS ====================
def router(state: InventoryState) -> str:
    """Route based on detected intent"""
    return state.get('intent', 'chitchat')


def has_tool_calls(state: InventoryState) -> str:
    """Check if analytics tools were called"""
    msgs = state.get("messages", [])
    if not msgs:
        return "end"
    last = msgs[-1]
    tool_calls = getattr(last, "tool_calls", None)
    return "tools" if tool_calls else "end"


# ==================== BUILD WORKFLOW ====================
print("🔧 Building workflow...")

# Create graph
graph = StateGraph(InventoryState)

# Add nodes
graph.add_node("supervisor_router", supervisor_router)
graph.add_node("products_handler", products_handler)
graph.add_node("bills_handler", bills_handler)
graph.add_node("suppliers_handler", suppliers_handler)
graph.add_node("customers_handler", customers_handler)
graph.add_node("analytics_insights", analytics_llm_node)
graph.add_node("analytics_tools", ToolNode(analytics_tools))
graph.add_node("analytics_formatter", analytics_formatter_node)
graph.add_node("executor_node", executor_node)
graph.add_node("response_node", response_node)
graph.add_node("chitchat_node", chitchat_node)

# Add edges
graph.add_edge(START, "supervisor_router")

# Conditional routing from supervisor
graph.add_conditional_edges(
    "supervisor_router",
    router,
    {
        "products": "products_handler",
        "suppliers": "suppliers_handler",
        "bills": "bills_handler",
        "customers": "customers_handler",
        "analytics": "analytics_insights",
        "chitchat": "chitchat_node"
    }
)

# Analytics flow
graph.add_conditional_edges(
    "analytics_insights",
    has_tool_calls,
    {
        "tools": "analytics_tools",
        "end": "analytics_formatter"
    }
)
graph.add_edge("analytics_tools", "analytics_formatter")
graph.add_edge("analytics_formatter", END)

# Data flow (products, bills, suppliers, customers)
graph.add_edge("products_handler", "executor_node")
graph.add_edge("bills_handler", "executor_node")
graph.add_edge("suppliers_handler", "executor_node")
graph.add_edge("customers_handler", "executor_node")

# Response flow
graph.add_edge("executor_node", "response_node")
graph.add_edge("response_node", END)

# Chitchat flow
graph.add_edge("chitchat_node", END)

# Compile workflow
checkpointer = InMemorySaver()
workflow = graph.compile(checkpointer=checkpointer)

print("✅ Workflow compiled successfully!")

 # ==================== EXPORT ====================
print("✅ Workflow ready!")


__all__ = ['workflow', 'InventoryState']   