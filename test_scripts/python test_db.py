"""
Database Connection & Data Checker
Tests MongoDB connection and checks for data
"""
from db.mongo_client import mongo_client
from dotenv import load_dotenv
import os

load_dotenv()

def test_database():
    """Test database connection and check data"""
    
    print("\n" + "="*60)
    print("🔍 DATABASE DIAGNOSTIC TEST")
    print("="*60)
    
    # 1. Test Connection
    print("\n1️⃣ Testing MongoDB Connection...")
    try:
        mongo_client.connect()
        print("✅ Connected successfully!")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return
    
    # 2. Get database
    db = mongo_client.db
    print(f"✅ Database: {db.name}")
    
    # 3. List all collections
    print("\n2️⃣ Collections in database:")
    collections = db.list_collection_names()
    for col in collections:
        count = db[col].count_documents({})
        print(f"   📁 {col}: {count} documents")
    
    # 4. Check products for specific owner
    owner_id = "jadhavshubham9718@gmail.com"
    print(f"\n3️⃣ Checking products for: {owner_id}")
    
    products_col = db["products"]
    
    # Count all products
    total = products_col.count_documents({})
    print(f"   Total products in database: {total}")
    
    # Count for this owner
    owner_products = products_col.count_documents({"owner": owner_id})
    print(f"   Products for {owner_id}: {owner_products}")
    
    # Show sample product
    if total > 0:
        print("\n4️⃣ Sample product from database:")
        sample = products_col.find_one({})
        print(f"   Owner: {sample.get('owner', 'N/A')}")
        print(f"   Name: {sample.get('name', 'N/A')}")
        print(f"   Category: {sample.get('category', 'N/A')}")
        print(f"   Stock: {sample.get('quantity', 'N/A')}")
    
    # 5. List all unique owners
    print("\n5️⃣ All owners in database:")
    owners = products_col.distinct("owner")
    for owner in owners:
        count = products_col.count_documents({"owner": owner})
        print(f"   👤 {owner}: {count} products")
    
    print("\n" + "="*60)
    print("✅ DIAGNOSTIC COMPLETE")
    print("="*60 + "\n")

if __name__ == "__main__":
    test_database()