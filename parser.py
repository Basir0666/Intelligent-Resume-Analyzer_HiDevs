from candidate import Candidate
import re


def parse_resume(resume_text):
    name = ""
    email = ""
    skills = []
    experience = 0
    education = ""

    lines = resume_text.split("\n")

    for line in lines:
        if 'name' in line.lower():
            if ':' in line:
                name = line.split(':')[1].strip()
        elif 'email' in line.lower():
            match = re.search(
                r'[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-z.]{2,}', line.lower())
            if match:
                email = match.group()
        elif 'skills' in line.lower():
            if ':' in line:
                skills = [s.strip() for s in (line.split(":")[1]).split(",")]
        elif 'experience' in line.lower():
            match = re.search(r'\d+', line)
            if match:
                experience = int(match.group())
        elif 'education' in line.lower():
            if ':' in line:
                education = line.split(":")[1].strip()

    return Candidate(name, email, skills, experience, education)
