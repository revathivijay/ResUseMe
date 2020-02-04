import spacy
from spacy.matcher import Matcher
from pdfToText import convert
import re
import pandas as pd
import  os
import csv
nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

def extract_name(resume_text):
    nlp_text = nlp(resume_text)
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    matcher.add('NAME', None, pattern)
    matches = matcher(nlp_text)

    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text

def extract_mobile_number(text):
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), text)

    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return '+' + number
        else:
            return number

def extract_email(email):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", email)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None

def extract_skills(resume_pdf):
    from pyresparser import ResumeParser
    data = ResumeParser(resume_pdf).get_extracted_data()
    skills = data['skills']
    text_skills = " ".join(skills)
    return skills, text_skills

def get_all_info(resume_pdf, filename):
    info = {}
    resume_text = convert(resume_pdf)
    name = extract_name(resume_text)
    email = extract_email(resume_text)
    mobile = extract_mobile_number(resume_text)
    skills, text_skills = extract_skills(resume_pdf)

    info['name'] = name
    info['email'] = email
    info['phone'] = mobile
    info['skills'] = skills
    cols = ['name', 'email', 'phone', 'skills']
    df = pd.DataFrame(info, columns=cols)
    print(df)
    df.to_csv(filename, mode='a')


resume_pdf = 'riya.pdf'
get_all_info(resume_pdf, 'info.csv')
# print(extract_name(convert(resume_pdf)))
