import pandas as pd


reference_skills = pd.read_csv('Skills.csv')
candidate_skills = pd.read_csv('info.csv')

category = "Web Developer"
unique_candidates = len(list(candidate_skills['name'].unique()))

reqd = list(reference_skills[category])
for i in range(len(reqd)):
    reqd[i].lower()

perc={}
for i in range(len(candidate_skills)):
    perc[candidate_skills['name'][i]]=0
    if not candidate_skills['skills'][i].islower():
        candidate_skills['skills'][i] = candidate_skills['skills'][i].lower()

for i in range(len(candidate_skills)):
    if any(candidate_skills['skills'][i] in s for s in reqd):
        perc[candidate_skills['name'][i]]+=1
