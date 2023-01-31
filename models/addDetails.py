from config import db 

class AddDetails(db.Model):
    __tablename__ = 'addDetails'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email_id = db.Column(db.String(200),nullable=False)
    resume_url=db.Column(db.String(200),nullable=False)
    skills=db.Column(db.String(200),nullable=False)
    age_group = db.Column(db.String(200),nullable=False)
    jobs_applied=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))