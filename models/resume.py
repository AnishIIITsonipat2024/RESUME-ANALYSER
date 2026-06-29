from app import db

class Resume(db.Model):
    __tablename__ = "resumes"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(200), nullable=False)

    ats_score = db.Column(db.Integer)

    skills = db.Column(db.Text)

    missing_skills = db.Column(db.Text)

    recommendation = db.Column(db.Text)

    upload_date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))