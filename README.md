# Yoruba Sentiment Analysis (Naive Bayes)

##  Live Demo  
Explore the web interface: [Try the app live](https://hz2cjqpzvcoasnprapdkyc.streamlit.app/)  

---

##  Overview  
This project develops a sentiment analysis system for **Yoruba text**, automatically classifying inputs into **Positive, Neutral, or Negative** categories.  
It contributes to **Natural Language Processing (NLP)** for African languages, particularly Yoruba, a low-resource language.  
Based on the **NaijaSenti** annotated tweets dataset.  

---

##  What the Project Does  
- **Data Preparation**: Cleaned and preprocessed Yoruba text—noise removal, tone-mark normalization, tokenization.  
- **Modeling**: Trained a **Naive Bayes classifier** to categorize tweets by sentiment.  
- **Evaluation**: Used **accuracy**, **precision**, **recall**, **F1-score**, and a **confusion matrix** to evaluate classification performance.  
- **Deployment**: Created a live **Streamlit app** enabling users to input Yoruba text and instantly receive predicted sentiment.

---

##  Significance  
- Enables **social media monitoring**, **customer feedback analysis**, and **opinion mining** in Yoruba.  
- Fills a crucial gap in computational tools for **Yoruba NLP**.  
- Demonstrates the applicability of lightweight models like **Naive Bayes** in low-resource settings.

---

##  Dependencies  
- Python 3.8+  
- pandas  
- numpy  
- scikit-learn  
- nltk  
- streamlit (for the interface)

---

##  Usage  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/yoruba-sentiment-analysis.git
   cd yoruba-sentiment-analysis
