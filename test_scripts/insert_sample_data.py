"""
Insert Sample Inventory Data
Run this ONCE to populate your database
"""
from db.mongo_client import mongo_client
from datetime import datetime, timezone, timedelta
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

def insert_sample_data():
    """Insert sample data for testing"""
    
    # Your email from the app
    owner_email = "jadhavshubham9718@gmail.com"
    
    print(f"\n🚀 Inserting sample data for: {owner_email}\n")
    
    # Connect to database
    mongo_client.connect()
    db = mongo_client.db
    
    # Check if data already exists
    existing = db.products.count_documents({"owner": owner_email})
    if existing > 0:
        print(f"⚠️  Found {existing} existing products. Delete them first? (y/n)")
        response = input().lower()
        if response == 'y':
            db.products.delete_many({"owner": owner_email})
            db.bills.delete_many({"owner": owner_email})
            db.suppliers.delete_many({"owner": owner_email})
            db.customers.delete_many({"owner": owner_email})
            print("✅ Cleared existing data")
        else:
            print("❌ Cancelled. Keeping existing data.")
            return
    
    # 1. Sample Products
    print("1️⃣ Inserting Products...")
    products = [
        {
            "owner": owner_email,
            "name": "Milk 1L",
            "category": "Dairy",
            "actualPrice": 45,
            "sellingPrice": 60,
            "quantity": 100,
            "reorderLevel": 20,
            "supplier": "Amul Dairy",
            "expirationDate": datetime.now(timezone.utc) + timedelta(days=7),
            "dateAdded": datetime.now(timezone.utc),
            "dateUpdated": datetime.now(timezone.utc)
        },
        {
            "owner": owner_email,
            "name": "Bread",
            "category": "Bakery",
            "actualPrice": 25,
            "sellingPrice": 40,
            "quantity": 50,
            "reorderLevel": 15,
            "supplier": "Britannia",
            "expirationDate": datetime.now(timezone.utc) + timedelta(days=2),
            "dateAdded": datetime.now(timezone.utc),
            "dateUpdated": datetime.now(timezone.utc)
        },
        {
            "owner": owner_email,
            "name": "Rice 5kg",
            "category": "Grains",
            "actualPrice": 180,
            "sellingPrice": 250,
            "quantity": 30,
            "reorderLevel": 10,
            "supplier": "India Gate",
            "expirationDate": datetime.now(timezone.utc) + timedelta(days=365),
            "dateAdded": datetime.now(timezone.utc),
            "dateUpdated": datetime.now(timezone.utc)
        },
        {
            "owner": owner_email,
            "name": "Yogurt 500g",
            "category": "Dairy",
            "actualPrice": 30,
            "sellingPrice": 45,
            "quantity": 15,
            "reorderLevel": 20,
            "supplier": "Amul Dairy",
            "expirationDate": datetime.now(timezone.utc) - timedelta(days=1),
            "dateAdded": datetime.now(timezone.utc),
            "dateUpdated": datetime.now(timezone.utc)
        },
        {
            "owner": owner_email,
            "name": "Cooking Oil 1L",
            "category": "Cooking",
            "actualPrice": 120,
            "sellingPrice": 160,
            "quantity": 25,
            "reorderLevel": 10,
            "supplier": "Fortune",
            "expirationDate": datetime.now(timezone.utc) + timedelta(days=180),
            "dateAdded": datetime.now(timezone.utc),
            "dateUpdated": datetime.now(timezone.utc)
        },
        {
            "owner": owner_email,
            "name": "Sugar 1kg",
            "category": "Groceries",
            "actualPrice": 35,
            "sellingPrice": 50,
            "quantity": 60,
            "reorderLevel": 15,
            "supplier": "Madhur",
            "expirationDate": datetime.now(timezone.utc) + timedelta(days=365),
            "dateAdded": datetime.now(timezone.utc),
            "dateUpdated": datetime.now(timezone.utc)
        },
        {
            "owner": owner_email,
            "name": "Tea Powder 250g",
            "category": "Beverages",
            "actualPrice": 80,
            "sellingPrice": 110,
            "quantity": 40,
            "reorderLevel": 10,
            "supplier": "Tata Tea",
            "expirationDate": datetime.now(timezone.utc) + timedelta(days=180),
            "dateAdded": datetime.now(timezone.utc),
            "dateUpdated": datetime.now(timezone.utc)
        },
        {
            "owner": owner_email,
            "name": "Biscuits Pack",
            "category": "Snacks",
            "actualPrice": 20,
            "sellingPrice": 30,
            "quantity": 80,
            "reorderLevel": 25,
            "supplier": "Parle",
            "expirationDate": datetime.now(timezone.utc) + timedelta(days=90),
            "dateAdded": datetime.now(timezone.utc),
            "dateUpdated": datetime.now(timezone.utc)
        }
    ]
    
    result = db.products.insert_many(products)
    print(f"✅ Inserted {len(result.inserted_ids)} products")
    
    # 2. Sample Bills
    print("\n2️⃣ Inserting Bills...")
    today = datetime.now(timezone.utc)
    
    bills = [
        {
            "owner": owner_email,
            "customerName": "Rajesh Kumar",
            "billNumber": f"BILL-{today.strftime('%Y%m%d')}-001",
            "date": today,
            "phoneNumber": "9876543210",
            "deposit": 240,
            "customerId": "CUST-001",
            "items": [
                {"productName": "Milk 1L", "quantity": 2, "price": 60, "total": 120},
                {"productName": "Bread", "quantity": 3, "price": 40, "total": 120}
            ],
            "grandTotal": 240,
            "netQuantity": 5,
            "history": [{
                "date": today,
                "depositHistory": 240,
                "paymentMethod": "Cash"
            }]
        },
        {
            "owner": owner_email,
            "customerName": "Priya Sharma",
            "billNumber": f"BILL-{today.strftime('%Y%m%d')}-002",
            "date": today,
            "phoneNumber": "9123456789",
            "deposit": 500,
            "customerId": "CUST-002",
            "items": [
                {"productName": "Rice 5kg", "quantity": 2, "price": 250, "total": 500}
            ],
            "grandTotal": 500,
            "netQuantity": 2,
            "history": [{
                "date": today,
                "depositHistory": 500,
                "paymentMethod": "Card"
            }]
        },
        {
            "owner": owner_email,
            "customerName": "Amit Patel",
            "billNumber": f"BILL-{today.strftime('%Y%m%d')}-003",
            "date": today,
            "phoneNumber": "9988776655",
            "deposit": 200,
            "customerId": "CUST-003",
            "items": [
                {"productName": "Sugar 1kg", "quantity": 2, "price": 50, "total": 100},
                {"productName": "Tea Powder 250g", "quantity": 1, "price": 110, "total": 110}
            ],
            "grandTotal": 210,
            "netQuantity": 3,
            "history": [{
                "date": today,
                "depositHistory": 200,
                "paymentMethod": "Cash"
            }]
        }
    ]
    
    result = db.bills.insert_many(bills)
    print(f"✅ Inserted {len(result.inserted_ids)} bills")
    
    # 3. Sample Suppliers
    print("\n3️⃣ Inserting Suppliers...")
    suppliers = [
        {
            "owner": owner_email,
            "supplierName": "Amul Dairy",
            "totalPayment": "50000",
            "depositAmount": "10000",
            "Date": today.isoformat(),
            "imageUrl": "",
            "createdAt": today,
            "updatedAt": today
        },
        {
            "owner": owner_email,
            "supplierName": "Britannia",
            "totalPayment": "30000",
            "depositAmount": "5000",
            "Date": today.isoformat(),
            "imageUrl": "",
            "createdAt": today,
            "updatedAt": today
        },
        {
            "owner": owner_email,
            "supplierName": "Parle",
            "totalPayment": "25000",
            "depositAmount": "8000",
            "Date": today.isoformat(),
            "imageUrl": "",
            "createdAt": today,
            "updatedAt": today
        }
    ]
    
    result = db.suppliers.insert_many(suppliers)
    print(f"✅ Inserted {len(result.inserted_ids)} suppliers")
    
    # 4. Sample Customers
    print("\n4️⃣ Inserting Customers...")
    customers = [
        {
            "owner": owner_email,
            "customerName": "Rajesh Kumar",
            "phoneNumber": "9876543210",
            "createdAt": today,
            "updatedAt": today
        },
        {
            "owner": owner_email,
            "customerName": "Priya Sharma",
            "phoneNumber": "9123456789",
            "createdAt": today,
            "updatedAt": today
        },
        {
            "owner": owner_email,
            "customerName": "Amit Patel",
            "phoneNumber": "9988776655",
            "createdAt": today,
            "updatedAt": today
        }
    ]
    
    result = db.customers.insert_many(customers)
    print(f"✅ Inserted {len(result.inserted_ids)} customers")
    
    print("\n" + "="*60)
    print("✅ SAMPLE DATA INSERTION COMPLETE!")
    print("="*60)
    print(f"\n📊 Summary for: {owner_email}")
    print(f"   Products: {db.products.count_documents({'owner': owner_email})}")
    print(f"   Bills: {db.bills.count_documents({'owner': owner_email})}")
    print(f"   Suppliers: {db.suppliers.count_documents({'owner': owner_email})}")
    print(f"   Customers: {db.customers.count_documents({'owner': owner_email})}")
    print(f"\n💡 Now run: streamlit run app.py")
    print()

if __name__ == "__main__":
    insert_sample_data()