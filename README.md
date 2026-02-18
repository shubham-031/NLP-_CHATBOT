# 🤖 Smart Inventory Management Chatbot
### AI-Powered Business Intelligence for Inventory Analytics

![Python](https://img.shields.io/badge/Python-90.7%25-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Architecture](#project-architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Features in Detail](#features-in-detail)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **Smart Inventory Management Chatbot** is an advanced AI-powered conversational interface designed to streamline inventory management and provide real-time business intelligence insights. Built with cutting-edge Natural Language Processing (NLP) technologies, this chatbot enables businesses to interact with their inventory data through natural language queries, generate analytics reports, and make data-driven decisions effortlessly.

### 🎪 What Makes It Smart?
- **Natural Language Understanding**: Ask questions in plain English
- **Real-time Analytics**: Get instant insights from your inventory data
- **Multi-Agent Architecture**: Powered by LangGraph for complex workflows
- **Business Intelligence**: Generate comprehensive reports and visualizations
- **MongoDB Integration**: Scalable database for inventory management
- **Conversational AI**: Context-aware responses using Google Generative AI

---

## ✨ Key Features

### 🗣️ Conversational Interface
- Natural language queries for inventory management
- Context-aware multi-turn conversations
- Intent recognition and entity extraction
- Personalized responses based on user role

### 📊 Business Intelligence & Analytics
- **Inventory Reports**: Stock levels, low stock alerts, expiry tracking
- **Sales Analytics**: Revenue analysis, trend identification
- **Predictive Insights**: Demand forecasting, reorder recommendations
- **Custom Dashboards**: Visual representation of key metrics
- **Export Capabilities**: PDF, CSV, Excel report generation

### 🔧 Inventory Operations
- Real-time stock level queries
- Product search and filtering
- Stock movement tracking
- Automated alerts for critical thresholds
- Multi-warehouse support

### 🤖 AI-Powered Features
- Intelligent query understanding
- Contextual follow-up questions
- Automated report generation
- Smart recommendations
- Learning from user interactions

---

## 🛠️ Technology Stack

### **Core Technologies**
| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Primary Language | 3.8+ |
| **Streamlit** | Web UI Framework | Latest |
| **LangChain** | LLM Framework | Latest |
| **LangGraph** | Agent Orchestration | Latest |
| **Google Generative AI** | LLM Provider | Latest |

### **Data & Database**
| Technology | Purpose |
|------------|---------|
| **MongoDB** | Primary Database |
| **PyMongo** | MongoDB Driver |
| **Pydantic** | Data Validation |

### **Development Tools**
- **Python-dotenv**: Environment configuration
- **Virtual Environment**: Dependency isolation
- **C++/Cython**: Performance optimization for ML libraries

### **Architecture Pattern**
- **Multi-Agent System**: LangGraph-based agent orchestration
- **MVC Pattern**: Separation of concerns
- **Modular Design**: Reusable components
- **Stateful Conversations**: Context management

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface (Streamlit)                │
└───────────────────────┬─────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Chatbot Runner (chatbot_runner.py)             │
│                  - Session Management                        │
│                  - Query Processing                          │
└───────────────────────┬─────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    LangGraph Workflow                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Intent Agent │→ │ Query Agent  │→ │ Response Gen │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└───────────────────────┬─────────────────────────────────────┘
                       │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Analytics  │ │   Database   │ │   Helpers    │
│     Module   │ │    Layer     │ │   Utilities  │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        └───────────────┼───────────────┘
                       ▼
                ┌──────────────┐
                │   MongoDB    │
                └──────────────┘
```

---

## 📁 Project Structure

```
NLP-_CHATBOT/
│
├── 📄 app.py                      # Main Streamlit application
├── 📄 chatbot_runner.py           # Chatbot orchestration logic
├── 📄 test_workflow.py            # Workflow testing scripts
├── 📄 requirements.txt            # Python dependencies
├── 📄 .env                        # Environment variables (DO NOT COMMIT)
├── 📄 README.md                   # Project documentation
│
├── 📂 models/                     # Data models and schemas
│   ├── __init__.py
│   └── state_models.py            # Pydantic state models for LangGraph
│
├── 📂 handlers/                   # Request handlers
│   └── [Intent handlers, Query processors]
│
├── 📂 db/                         # Database layer
│   └── [MongoDB connection, CRUD operations]
│
├── 📂 analytics/                  # Business intelligence module
│   ├── __init__.py
│   ├── analytics_llm.py           # LLM-powered analytics
│   └── analytics_tools.py         # Analytics tools & functions
│
├── 📂 utils/                      # Utility functions
│   ├── __init__.py
│   └── helpers.py                 # Helper functions
│
├── 📂 test_scripts/               # Testing scripts
│   └── [Unit tests, Integration tests]
│
└── 📂 venv/                       # Virtual environment (gitignored)
```

### 📦 Module Descriptions

#### **Core Modules**
- **app.py**: Streamlit-based web interface with chat UI
- **chatbot_runner.py**: Main chatbot logic and LangGraph workflow execution

#### **Models**
- **state_models.py**: Pydantic models for conversation state management

#### **Analytics**
- **analytics_llm.py**: LLM integration for intelligent analytics
- **analytics_tools.py**: Analytics functions (reports, charts, metrics)

#### **Database**
- MongoDB operations for inventory data
- CRUD operations for products, transactions, users

#### **Utilities**
- **helpers.py**: Common utility functions
- Data formatters, validators, converters

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- MongoDB instance (local or cloud)
- Google AI API key (for Generative AI)
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/shubham-031/NLP-_CHATBOT.git
cd NLP-_CHATBOT
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory:
```env
# Google AI Configuration
GOOGLE_API_KEY=your_google_api_key_here

# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DATABASE=inventory_db

# Application Configuration
APP_ENV=development
DEBUG=True
```

### Step 5: Initialize Database
```bash
python test_workflow.py  # Run initial setup
```

---

## ⚙️ Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Generative AI API key | ✅ Yes |
| `MONGODB_URI` | MongoDB connection string | ✅ Yes |
| `MONGODB_DATABASE` | Database name | ✅ Yes |
| `APP_ENV` | Environment (dev/prod) | ⚠️ Optional |
| `DEBUG` | Enable debug mode | ⚠️ Optional |

---

## 💻 Usage

### Running the Application

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Run Streamlit app
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Example Queries

```
📦 Inventory Queries:
- "Show me current stock levels for Product X"
- "Which items are running low on stock?"
- "What products are expiring this month?"

📊 Analytics:
- "Generate a sales report for last quarter"
- "Show me the top 10 selling products"
- "What's the inventory turnover ratio?"

🔔 Alerts:
- "Set up low stock alerts for critical items"
- "Show me products below reorder point"

📈 Predictions:
- "Predict demand for next month"
- "Which items should I reorder?"
```

---

## 🎯 Features in Detail

### 1️⃣ Multi-Agent Architecture
The chatbot uses LangGraph to orchestrate multiple specialized agents:
- **Intent Classification Agent**: Understands user queries
- **Database Query Agent**: Retrieves data from MongoDB
- **Analytics Agent**: Processes and analyzes data
- **Response Generation Agent**: Crafts natural language responses

### 2️⃣ Conversation State Management
- Maintains context across multiple turns
- Remembers user preferences
- Handles follow-up questions intelligently

### 3️⃣ Business Intelligence
- Real-time dashboards
- Automated report generation
- Trend analysis and forecasting
- KPI tracking

---

## 📚 API Documentation

### Chatbot Runner API
```python
from chatbot_runner import ChatbotRunner

# Initialize chatbot
chatbot = ChatbotRunner()

# Process query
response = chatbot.process_query(
    user_query="Show inventory levels",
    session_id="user_123"
)
```

### Analytics API
```python
from analytics import generate_report

# Generate analytics report
report = generate_report(
    report_type="inventory_summary",
    date_range="last_30_days"
)
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Shubham**
- GitHub: [@shubham-031](https://github.com/shubham-031)

---

## 🙏 Acknowledgments

- LangChain team for the amazing framework
- Google for Generative AI capabilities
- Streamlit for the beautiful UI framework
- MongoDB for scalable database solutions

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [Your Email]

---

**⭐ Star this repository if you find it helpful!**