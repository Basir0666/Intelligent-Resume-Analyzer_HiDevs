def requirement_input():
    job_title = input("Enter Job Title: ").title()
    skills = input("Required skills (comma separated): ")
    while True:
        try:
            min_experience = int(input("Minimum experience (in years): "))
            break
        except ValueError:
            print("Please enter a number.")

    education = input("Required education: ").title()

    job_requirement = {
        "title": job_title,
        "skills": [s.strip().title() for s in skills.split(",")],
        "min_experience": min_experience,
        "education": education
    }

    return job_requirement
