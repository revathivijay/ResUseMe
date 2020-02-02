import pandas as pd
import operator
reference_skills = pd.read_csv('./Main/Skills.csv')
candidate_skills = pd.read_csv('./Main/info.csv')
import warnings
from Main.scraping import scraper
warnings.filterwarnings('ignore')

def match(category, reference_skills=reference_skills, candidate_skills=candidate_skills):
    scraper(category)
    reference_skills_df = reference_skills[category]
    reference_skills_df = reference_skills_df.dropna()
    candidate_skills = candidate_skills.drop('Unnamed: 0', axis=1)
    candidate_skills = candidate_skills.dropna()
    print(candidate_skills.columns)
    unique_candidates = len(list(candidate_skills['name'].unique()))
    # unique_candidates

    reqd = list(reference_skills_df)
    # print(reqd)
    for i in range(len(reqd)):
        reqd[i] = reqd[i].lower()

    perc={}
    for i in range(len(candidate_skills)):
        # print("HI", candidate_skills['name'][i])
        perc[candidate_skills['name'][i]]=0
        if not candidate_skills['skills'][i].islower():
            candidate_skills['skills'][i] = candidate_skills['skills'][i].lower()

    for i in range(len(candidate_skills)):
        if any(candidate_skills['skills'][i] in s for s in reqd):
            perc[candidate_skills['name'][i]]+=1
            # print(candidate_skills['skills'][i])
    total = len(reqd)
    for key, value in perc.items():
        perc[key] = float(value/total*100)

    sorted_perc = sorted(perc.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_perc)
    new_sort=[]
    for i in range(len(sorted_perc)):
        li = []
        if(sorted_perc[i][1]==0):
            break;
        li.append(sorted_perc[i][0])
        if sorted_perc[i][1]*2.7>=89.67:
            li.append(89.67)
        elif sorted_perc[i][1]!=0:
            li.append(sorted_perc[i][1]*2.7)
        new_sort.append(li)
    # print(new_sort)
    # print(new_sort[:5])


    return new_sort[:10], reqd
