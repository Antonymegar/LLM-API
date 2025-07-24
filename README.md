🚀 FastAPI Gemini LLM API
This project provides a simple /chat API endpoint using Google Gemini (via Generative AI SDK) to generate responses to user prompts.

🔧 Setup Instructions
1. Clone the project
   git clone https://github.com/yourusername/your-repo.git](https://github.com/Antonymegar/LLM-API.git
   cd pawallm-api
2. Create & activate virtual environment
   python3 -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies
   pip install -r requirements.txt
4. Set up environment variables
   Create a .env file in the root directory and add your Gemini API key:
   GEMINI_API_KEY=your_google_ai_key_here
   Get your API key from(https://aistudio.google.com/app/apikey)

▶️ Running the App
Start the FastAPI server:
fastapi dev main.py
The API will be available at:
http://localhost:8000/chat
Swagger Doc 
http://localhost:8000/docs
