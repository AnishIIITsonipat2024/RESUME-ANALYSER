required_skills = [
    "Python",
    "Flask",
    "SQL",
    "Git",
    "Docker",
    "React",
    "TensorFlow",
    "PyTorch"
]

def find_missing(text):

    missing = []

    for skill in required_skills:

        if skill.lower() not in text.lower():
            missing.append(skill)

    return missing