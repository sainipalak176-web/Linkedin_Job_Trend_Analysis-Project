import pandas as pd
import random

# Sample data banayenge (jaisa LinkedIn job postings hota hai)
cities = ["Bangalore", "Mumbai", "Delhi", "Hyderabad", "Pune", "Chennai"]
roles = ["Data Analyst", "Data Scientist", "Software Engineer", "Business Analyst", "ML Engineer"]
skills_pool = ["Python", "SQL", "Excel", "Power BI", "Tableau", "Machine Learning",
               "Java", "AWS", "Communication", "Deep Learning", "Statistics", "R"]

data = []
for i in range(500):
    job = {
        "Job_Title": random.choice(roles),
        "City": random.choice(cities),
        "Skill": random.choice(skills_pool)
    }
    data.append(job)

df = pd.DataFrame(data)

# CSV file mein save karo
df.to_csv("linkedin_jobs.csv", index=False)

print("Data ban gaya! Total rows:", len(df))
print(df.head())