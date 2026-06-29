from flask import Blueprint, render_template, request

analysis = Blueprint("analysis", __name__)

@analysis.route("/result")
def result():

    filename = request.args.get("filename")

    # Dummy output
    score = 88
    skills = [
        "Python",
        "Machine Learning",
        "Flask",
        "SQL"
    ]

    suggestions = [
        "Add GitHub link",
        "Improve project descriptions",
        "Mention achievements"
    ]

    return render_template(
        "result.html",
        filename=filename,
        score=score,
        skills=skills,
        suggestions=suggestions
    )