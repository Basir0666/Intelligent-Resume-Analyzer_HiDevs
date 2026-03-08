def matching_education(candidate_education, required_education):
    bachelor = ['bachelor', 'bachelors', 'b.tech', 'b.a', 'b.sc',
                'b.com', 'bba', 'bca', 'btech', 'ba', 'bsc', 'bcom']
    masters = ['master', 'masters', 'm.a', 'm.sc',
               'm.tech', 'ma', 'msc', 'mtech', 'mba', 'mca']
    phd = ['phd']
    if required_education.lower() in bachelor:
        if candidate_education.lower() in (bachelor+masters+phd):
            return True
    elif required_education.lower() in masters:
        if candidate_education.lower() in (masters+phd):
            return True
    elif required_education.lower() in phd:
        if candidate_education.lower() in phd:
            return True
    return False


def match_candidate(candidate, job_requirements):

    score = 0

    candidate_skills = [s.lower() for s in candidate["skills"]]
    job_requirements_skills = [s.lower() for s in job_requirements["skills"]]

    skills_matched = len(set(candidate_skills) &
                         set(job_requirements_skills))
    score += skills_matched*10

    if candidate['experience'] >= job_requirements["min_experience"]:
        score += 30
    if matching_education(candidate['education'], job_requirements["education"]):
        score += 20

    return min(score, 100)
