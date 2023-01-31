from config import db 
class JobsForStudents(db.Model):
    __tablename__ = 'jobsForStudents'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    job_desc=db.Column(db.String(200),nullable=False)
    salary_expected=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))