import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

import re

import nltk
from nltk.corpus import stopwords
import string
import pickle

#revathi imports
from cleanDataset import cleanResume
from pdfToText import convert
from extractDetails import extract_name, extract_email, extract_skills, extract_mobile_number
from scraping import scraper

labels = {'Advocate': 0, 'Arts': 1, 'Automation Testing': 2, 'Blockchain': 3, 'Business Analyst': 4, 'Civil Engineer': 5, 'Data Science': 6, 'Database': 7, 'DevOps Engineer': 8, 'DotNet Developer': 9, 'ETL Developer': 10, 'Electrical Engineering': 11, 'HR': 12, 'Hadoop': 13, 'Health and fitness': 14, 'Java Developer': 15, 'Mechanical Engineer': 16, 'Network Security Engineer': 17, 'Operations Manager': 18, 'PMO': 19, 'Python Developer': 20, 'SAP Developer': 21, 'Sales': 22, 'Testing': 23, 'Web Designing': 24}

resumeDataSet = pd.read_csv('resume_dataset.csv' ,encoding='utf-8')
resumeDataSet['cleaned_resume'] = ''
resumeDataSet['encodedCategory'] = resumeDataSet['Category'].copy()

resumeDataSet['cleaned_resume'] = resumeDataSet.Resume.apply(lambda x: cleanResume(x))
oneSetOfStopWords = set(stopwords.words('english')+['``',"''"])
totalWords =[]
Sentences = resumeDataSet['Resume'].values
cleanedSentences = ""
for i in range(0,160):
    cleanedText = cleanResume(Sentences[i])
    cleanedSentences += cleanedText
    requiredWords = nltk.word_tokenize(cleanedText)
    for word in requiredWords:
        if word not in oneSetOfStopWords and word not in string.punctuation:
            totalWords.append(word)

wordfreqdist = nltk.FreqDist(totalWords)
mostcommon = wordfreqdist.most_common(50)
# print("MOST COMMON", mostcommon)

from sklearn.preprocessing import LabelEncoder
var_mod = ['encodedCategory']
le = LabelEncoder()
# labels = []
for i in var_mod:
    resumeDataSet[i] = le.fit_transform(resumeDataSet[i])
    le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    # labels.append(le_name_mapping)
    # print(le_name_mapping)
# print ("CONVERTED THE CATEGORICAL VARIABLES INTO NUMERICALS")
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack

requiredText = resumeDataSet['cleaned_resume'].values
requiredTarget = resumeDataSet['encodedCategory'].values

word_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='word',
    token_pattern=r'\w{1,}',
    stop_words='english',
    ngram_range=(1, 1),
    max_features=2000)
word_vectorizer.fit(requiredText)
WordFeatures = word_vectorizer.transform(requiredText)

char_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='char',
    stop_words='english',
    ngram_range=(2, 6),
    max_features=2000)
char_vectorizer.fit(requiredText)
CharFeatures = char_vectorizer.transform(requiredText)
totalFeatures = hstack([WordFeatures, CharFeatures])
word_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    stop_words='english',
    max_features=10000)
word_vectorizer.fit(requiredText)
WordFeatures = word_vectorizer.transform(requiredText)

X_train,X_test,y_train,y_test = train_test_split(WordFeatures,requiredTarget,random_state=0, test_size=0.2)

clf = OneVsRestClassifier(KNeighborsClassifier(n_neighbors=4))
clf.fit(X_train, y_train)
prediction = clf.predict(X_test)
# print('Accuracy of KNeighbors Classifier on training set: {:.2f}'.format(clf.score(X_train, y_train)))
# print('Accuracy of KNeighbors Classifier on test set: {:.2f}'.format(clf.score(X_test, y_test)))
#
# print("\n Classification report for classifier %s:\n%s\n" % (clf, metrics.classification_report(y_test, prediction)))

"""SAVING THE MODEL"""
filename = 'final.pkl'
pickle.dump(clf, open(filename, 'wb'))

def predict_model(filename):
    skills, text_skills = extract_skills(filename)
    # variable1 = convert(filename)
    cleaned_resume = cleanResume(text_skills)
    cleaned_resume = [cleaned_resume]
    WordFeatures = word_vectorizer.transform(cleaned_resume)
    pred = clf.predict(WordFeatures)
    str_pred = list(le_name_mapping.keys())[list(le_name_mapping.values()).index(pred)]
    # print("Prediction:", str_pred)
    return str_pred

def get_info_from_dir():
    files = []
    import os
    for file in os.listdir("resumes/"):
        if file.endswith(".pdf"):
            files.append(os.path.join("resumes/", file))
    preds = {}
    info = {}
    for file in files:
        f = convert(file)
        info['name'] = extract_name(f)
        info['email'] = 'dummy@example.com'
        info['phone'] = '555-5555-555'
        skill, str = extract_skills(file)
        info['skills'] = skill
        info['category'] = "".join(predict_model(file))
        df = pd.DataFrame(info)
        df.to_csv(filename, mode='a')
