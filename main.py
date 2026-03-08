
from file_manager import load_from_file, save_to_file
from parser import parse_resume
from matcher import match_candidate
from reporter import generate_analysis_report
from resume_importer import resume_input
from job_requirement_importer import requirement_input

if __name__ == "__main__":
    print(":::::::: Welcome to Intelligent Resume Analyzer ::::::::")

    resume_file = resume_input()
    resume_text = load_from_file(resume_file)
    job_requirement = requirement_input()

    candidate = parse_resume(resume_text).to_dict()

    score = match_candidate(candidate, job_requirement)

    report = generate_analysis_report(candidate, job_requirement, score)

    save_file_name = f'{candidate["name"]}_report.json'
    save_to_file(save_file_name, report)
