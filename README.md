# 📩 SMS Spam Detection using Machine Learning

This project is a simple yet powerful **SMS Spam Classifier** built with **Python, Scikit-learn, and Streamlit**.  
It predicts whether a given text message is **Spam** or **Not Spam** using a trained machine learning model.

---

Try it out here: [Click here](https://sms-spamm-detection.streamlit.app)

## 🚀 Features
- Clean and simple **web interface** built with **Streamlit**
- Real-time SMS classification  
- Pre-trained **TF-IDF Vectorizer** and **Logistic Regression** model  
- Lightweight and easy to deploy anywhere  

---

## 🧠 Model Training
The model was trained on a labeled SMS dataset containing spam and ham (non-spam) messages.  
Steps involved:
1. Data preprocessing (removing stopwords, punctuation, etc.)
2. Text vectorization using **TF-IDF**
3. Model training and evaluation
4. Model and vectorizer exported via **pickle**

---

## 💻 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/sms-spam-detection.git
cd sms-spam-detection
```
### 2️⃣ Run the app
```bash
streamlit run app.py
```
