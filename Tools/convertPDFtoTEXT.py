from pyresparser import ResumeParser
import spacy
spacy.load("en_core_web_sm")
data = ResumeParser("pdf_name").get_extracted_data()
print(data)
