import streamlit as st
import nltk
import string
import pickle
import warnings
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
# from nltk.corpus import stopwords
from joblib import load
ps= PorterStemmer()


# nltk.download('punkt')
# ps.stem
# from sklearn.feature_extraction.text import TfidfVectorizer
# tfidf= TfidfVectorizer()

# from sklearn.exceptions import InconsistentVersionWarning
# warnings.simplefilter("error", InconsistentVersionWarning)

# try:
#    model = pickle.load(open('rfc_model.pkl','rb'))
# except InconsistentVersionWarning as w:
#    print(w.original_sklearn_version)

tfidf= pickle.load(open('vectorizer.pkl','rb'))
model= pickle.load(open('rfc_model.pkl','rb'))
st.title('Email/SMS spam classifier')


# nltk.download('stopwords', download_dir='E:/projects_I_will_never_do/pp_repo/personal_projects/ML_Email_spam_classifier')
# nltk.data.path.append('E:/projects_I_will_never_do/pp_repo/personal_projects/ML_Email_spam_classifier')
# stop_words = set(stopwords.words('english'))

             
# model= load('model.joblib')
# model= pickle.load(open('rfc_model.pkl','rb'))




def transform_text(text):
    # text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


input_sms= st.text_input("Enter the message")
transformed_sms= transform_text(input_sms)
vector_input= tfidf.transform([transformed_sms])
result= model.predict(vector_input)[0]


if result==1:
    st.header("SPAMMMMMM")
else:
    st.header("not spam :))))")


