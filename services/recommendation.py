def recommend_jobs(text):

    jobs = []

    if "flask" in text.lower():
        jobs.append("Backend Developer")

    if "react" in text.lower():
        jobs.append("Full Stack Developer")

    if "tensorflow" in text.lower():
        jobs.append("Machine Learning Engineer")

    if "pytorch" in text.lower():
        jobs.append("AI Engineer")

    return jobs