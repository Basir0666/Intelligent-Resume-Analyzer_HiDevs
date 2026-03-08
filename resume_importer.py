def resume_input():
    print("Enter your resume details:")
    name = input("Name: ")
    email = input("Email: ")
    skills = input("Skills (comma separated): ")
    experience = input("Experience (in years): ")
    education = input("Education: ")

    # Format it the same way your parser expects
    resume_text = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Skills: {skills}\n"
        f"Experience: {experience}\n"
        f"Education: {education}"
    )

    filename = f'{name} resume.txt'

    # Save it to a fixed file
    with open(filename, "w") as f:
        f.write(resume_text)

    return filename
