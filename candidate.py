class Candidate:
    def __init__(self, name: str, email: str, skills: list[str], experience: int, education: str):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience
        self.education = education

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "skills": self.skills,
            "experience": self.experience,
            "education": self.education
        }
