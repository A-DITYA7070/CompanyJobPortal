from config import db 
class PostInternships(db.Model):
    __tablename__ = 'postInternships'
    id=db.Column(db.Integer,primary_key=True)
    location = db.Column(db.String(200),nullable=False)
    company_name = db.Column(db.String(200),nullable=False)
    intern_type = db.Column(db.String(200),nullable=False)
    resume_url=db.Column(db.String(200),nullable=False)
    skills=db.Column(db.String(200),nullable=False)
    role = db.Column(db.String(200),nullable=False)
    salary_expected=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))