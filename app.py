from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def analyze_resume(text):
    text = text.lower()

    # Skill categories
    skill_keywords = {
        "Python": ["python"],
        "Java": ["java"],
        "Machine Learning": ["machine learning", "ml", "deep learning"],
        "Web Development": ["html", "css", "javascript"],
        "Database": ["mysql", "sql"],
        "Git": ["git"],
        "REST API": ["rest", "api"]
    }

    detected_skills = []
    score = 0

    for skill, keywords in skill_keywords.items():
        for keyword in keywords:
            if keyword in text:
                detected_skills.append(skill)
                score += 10
                break

    # Experience level estimation
    if score >= 60:
        level = "Advanced"
    elif score >= 30:
        level = "Intermediate"
    else:
        level = "Beginner"

    # Missing important skills
    high_demand = ["Git", "REST API", "Cloud", "Docker"]
    missing_skills = []

    for skill in high_demand:
        if skill.lower() not in text:
            missing_skills.append(skill)

    suggestions = [
        "Quantify project achievements with metrics",
        "Mention REST API development experience",
        "Include deployment or cloud experience"
    ]

    return {
        "detected_skills": detected_skills,
        "skill_score": score,
        "experience_level": level,
        "missing_skills": missing_skills,
        "suggestions": suggestions,
        "recommended_roles": [
            "Application Developer",
            "Software Engineer",
            "AI Engineer"
        ]
    }

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    resume_text = data.get("resume_text", "")
    result = analyze_resume(resume_text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)