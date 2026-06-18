# Job roles and required skills

jobs = {
    "Data Scientist": ["python", "sql", "machine learning"],
    "Data Analyst": ["excel", "sql", "power bi"],
    "Web Developer": ["html", "css", "javascript"],
    "Software Developer": ["python", "java", "git"],
    "AI Engineer": ["python", "machine learning", "deep learning"]
}

# Get user skills
user_input = input("Enter your skills (comma separated): ")

# Convert input into a list
user_skills = user_input.lower().split(",")

# Remove extra spaces
for i in range(len(user_skills)):
    user_skills[i] = user_skills[i].strip()

best_job = ""
highest_match = 0

# Check each job role
for job, skills in jobs.items():

    match_count = 0

    for skill in skills:
        if skill in user_skills:
            match_count += 1

    if match_count > highest_match:
        highest_match = match_count
        best_job = job

# Show result
print("\n===== RESULT =====")
print("Recommended Job Role:", best_job)

# Show missing skills
print("\nSkills to Learn:")

for skill in jobs[best_job]:
    if skill not in user_skills:
        print("-", skill)