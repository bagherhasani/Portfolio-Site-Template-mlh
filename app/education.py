from flask import Blueprint, render_template

education_bp = Blueprint('education', __name__)

EDUCATION_ENTRIES = [
    {
        "school": "University of Tulsa",
        "degree": "BS Computer Science — Minor in Artificial Intelligence & Mathematics",
        "dates": "2023 – Present",
        "description": (
            "Majoring in Computer Science with minors in Artificial Intelligence and Mathematics, "
            "and working as an undergraduate robotics researcher at the Institute for Robotics and Autonomy. "
            "Clubs: Software Engineering Club, Artificial Intelligence Club. "
            "Relevant coursework: Java Programming, Data Structures, Algorithms, Assembly Language Programming, "
            "Programming Languages, Physics II, Numerical Methods, Interaction Design, Introduction to Cybersecurity."
        ),
    },
]


@education_bp.route('/education')
def education():
    return render_template('education.html', title="Education", entries=EDUCATION_ENTRIES)
