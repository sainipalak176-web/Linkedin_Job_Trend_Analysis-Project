import pandas as pd
import matplotlib.pyplot as plt

# CSV file read karo
df = pd.read_csv("linkedin_jobs.csv")

print("Total Jobs:", len(df))
print("\nTop Cities:\n", df['City'].value_counts())
print("\nTop Skills:\n", df['Skill'].value_counts())

# Chart 1: Top Skills Bar Graph
plt.figure(figsize=(8,5))
df['Skill'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Top Skills in Demand")
plt.xlabel("Skill")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("top_skills.png")
plt.show()

# Chart 2: City-wise Job Count
plt.figure(figsize=(8,5))
df['City'].value_counts().plot(kind='bar', color='orange')
plt.title("Job Demand by City")
plt.xlabel("City")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("jobs_by_city.png")
plt.show()
print("\n--- Skill vs Role Matrix ---")
matrix = pd.crosstab(df['Job_Title'], df['Skill'])
print(matrix)
matrix.to_csv("skill_vs_role_matrix.csv")

print("\n--- Job Demand Recommendation ---")
top_city = df['City'].value_counts().idxmax()
top_skill = df['Skill'].value_counts().idxmax()
print(f"Highest job demand city: {top_city}")
print(f"Most in-demand skill: {top_skill}")
print(f"Recommendation: Candidates should focus on '{top_skill}' skill and consider opportunities in '{top_city}'.")