import json


def load_from_file(filename):
    try:
        with open(filename, "r") as f:
            resume_text = f.read()
        return resume_text
    except FileNotFoundError:
        return None


def save_to_file(filename, report):
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
