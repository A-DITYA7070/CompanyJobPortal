from config import db 
class ListJobsForEveryone(db.Model):
    __tablename__ = 'listJobsForEveryone'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    company_name = db.Column(db.String(200),nullable=False)
    skills=db.Column(db.String(200),nullable=False)
    job_desc=db.Column(db.String(200),nullable=False)
    role = db.Column(db.String(200),nullable=False)
    salary_expected=db.Column(db.String(200),nullable=False)
    job_type=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))