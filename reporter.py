from matcher import matching_education


def recommendation_system(score):
    if score >= 80:
        return "✅ STRONGLY RECOMMEND"
    elif score >= 60:
        return "✓ RECOMMEND"
    elif score >= 40:
        return "⚠ MAYBE"
    else:
        return "✗ NOT RECOMMENDED"


def generate_analysis_report(candidate, job_requirement, score):

    candidate_skills = [s.lower() for s in candidate["skills"]]
    job_requirements_skills = [s.lower() for s in job_requirement["skills"]]
    matched_skills = set(candidate_skills) & set(job_requirements_skills)
    not_matched = ', '.join(
        list(set(job_requirements_skills) - matched_skills))
    if not_matched == '':
        not_matched = 'None'

    report = {
        "candidate": candidate['name'],
        "job": job_requirement["title"],
        "match_score": f'{score}/100',
        "skills_analysis": f'• Matched: {len(matched_skills)}/{len(set(job_requirement["skills"]))}\n• Missing: {not_matched}',
        "recommendation": f'{recommendation_system(score)}',
        "experience_passed": candidate['experience'] >= job_requirement["min_experience"],
        "education_matched": matching_education(candidate['education'], job_requirement["education"])

    }
    print(f"""
    ===== CANDIDATE ANALYSIS REPORT =====
    Candidate: {report["candidate"]}
    Job: {report['job']}
    Match Score: {report['match_score']}
    Education : {'Passed' if report["education_matched"] else 'Failed'}
    Experience : {'Passed' if report['experience_passed'] else 'Failed'}
    SKILLS ANALYSIS:
    • Matched: {len(matched_skills)}/{len(set(job_requirement["skills"]))}
    • Missing: {not_matched}
    RECOMMENDATION: {report['recommendation']}
    """)
    return report
