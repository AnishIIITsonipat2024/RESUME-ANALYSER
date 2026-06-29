def calculate_ats(text):

    score = 50

    keywords = [
        "python",
        "sql",
        "flask",
        "react",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "docker",
        "git"
    ]

    for word in keywords:
        if word.lower() in text.lower():
            score += 5

    if score > 100:
        score = 100

    return score