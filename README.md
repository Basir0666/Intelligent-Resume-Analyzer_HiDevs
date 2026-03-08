# Intelligent Resume Analyzer

A Python-based application that automates resume screening by parsing resumes,
matching candidates to job requirements, and generating detailed analysis reports.


## Project Structure
- `candidate.py` — Candidate data class
- `parser.py` — Resume text parser
- `matcher.py` — Scoring and matching logic
- `reporter.py` — Report generation
- `file_manager.py` — JSON file operations
- `resume_importer.py` — Resume input collector
- `job_requirement_importer.py` — Job requirement input collector
- `main.py` — Entry point

## How to Run
1. Clone the repository
2. Run the following command:
   python main.py
3. Enter your resume details when prompted
4. Enter job requirement details when prompted
5. A JSON report will be saved automatically

## Scoring System
| Score | Recommendation |
|-------|---------------|
| 80-100 | ✅ Strongly Recommend |
| 60-79  | ✓ Recommend |
| 40-59  | ⚠ Maybe |
| 0-39   | ✗ Not Recommended |

##  Features
- Resume parsing from text input
- Skill matching with case insensitive comparison
- Education level hierarchy matching
- Experience validation
- JSON report generation

## Demo Video
[![Resume Analyzer Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
