"""Test if workflow can be imported and run"""
import sys
import os

# Add path
sys.path.insert(0, r'D:\NLP CHATBOT INVENTORY\GenAI')

print("Testing workflow...\n")

try:
    from chatbot_runner import workflow, InventoryState
    print("✅ Workflow imported successfully")
    
    # Test simple query
    state = {
        "owner_id": "test@example.com",
        "user_query": "Hello",
        "messages": []
    }
    
    config = {
        "configurable": {
            "thread_id": "test-123"
        }
    }
    
    print("\n🔄 Running test query...")
    result = workflow.invoke(input=state, config=config)
    
    print(f"\n✅ Response: {result.get('response', 'No response')}")
    print("\n✅ Workflow is working!")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()