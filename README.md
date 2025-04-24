## 📜 Description

- This **Healthcare ChatBot** uses **Gemini 1.5 Pro** to assist users with health-related inquiries.
- It can analyze patient-reported symptoms, offer preliminary diagnoses, suggest possible conditions, and provide tailored health recommendations.
- Designed to be intuitive and responsive, the chatbot is ideal for guiding users toward informed medical decisions and identifying potential health trends.



## 🌟 Features

- **Real-Time Symptom Analysis:** Analyzes user-reported symptoms and offers insights into possible health conditions.
- **Personalized Health Recommendations:** Provides guidance on next steps for medical care and suggests preventive measures based on symptoms.
- **Interactive and User-Friendly Interface:** Built with Streamlit for seamless user interaction and real-time response display.
- **Integrated with Google Generative AI SDK:** Utilizes the Gemini 1.5 Pro model for advanced text generation and natural language understanding.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Libraries:** Streamlit, dotenv, google-generativeai
- **API:** Google Generative AI SDK with Gemini 1.5 Pro Model
- **Frontend:** Streamlit framework

## 🚀 Installation and Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vamshikrishna72/AI-Symptom-Checker.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd HealthMate
   ```

3. **Create a Virtual Environment (if not already created):**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   python.exe -m pip install --upgrade pip
   ```

6. **Set Up Environment Variables:**
   - Create a `.env` file in the project directory and add your **Gemini API key**:
     ```plaintext
     GEMINI_API_KEY=your_api_key_here
     ```

7. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

8. **Access the App:**
   - Open a web browser and go to `http://localhost:8501`.

## 🌐 Web Page

   deoployement phase
