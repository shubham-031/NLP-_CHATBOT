from typing import Dict, Any, List
from .mongo_client import mongo_client


class MongoExecutor:
    """Execute MongoDB queries"""
    
    def __init__(self):
        if mongo_client.db is None:
            mongo_client.connect()
    
    def execute_single(
        self, 
        collection_name: str, 
        filter_query: Dict[str, Any], 
        owner_id: str
    ) -> List[Dict[str, Any]]:
        """
        Execute a single query on a collection
        
        Args:
            collection_name: Name of the collection
            filter_query: MongoDB filter
            owner_id: Owner ID for filtering
            
        Returns:
            List of documents
        """
        try:
            # Ensure owner filter
            if "owner" not in filter_query:
                filter_query["owner"] = owner_id
            
            # Get collection
            collection = mongo_client.get_collection(collection_name)
            
            # Execute query
            results = list(collection.find(filter_query))
            
            # Convert ObjectId to string for JSON serialization
            for doc in results:
                if "_id" in doc:
                    doc["_id"] = str(doc["_id"])
            
            print(f"✅ Found {len(results)} documents in {collection_name}")
            return results
            
        except Exception as e:
            print(f"❌ Query Error in {collection_name}: {e}")
            return []
    
    def execute_aggregation(
        self, 
        collection_name: str, 
        pipeline: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Execute aggregation pipeline
        
        Args:
            collection_name: Name of the collection
            pipeline: Aggregation pipeline
            
        Returns:
            List of aggregated results
        """
        try:
            collection = mongo_client.get_collection(collection_name)
            results = list(collection.aggregate(pipeline))
            
            # Convert ObjectId to string
            for doc in results:
                if "_id" in doc and doc["_id"] is not None:
                    doc["_id"] = str(doc["_id"])
            
            return results
            
        except Exception as e:
            print(f"❌ Aggregation Error in {collection_name}: {e}")
            return []