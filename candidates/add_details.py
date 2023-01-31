from config import db

class Add_details(db.Model):
    __tablename__ = 'add_details'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    email_id=db.Column(db.String(200),nullable=False)
    skills = db.Column(db.String(200),nullable=False)
    agegroup = db.Column(db.String(200),nullable=False)
    resume_link = db.Column(db.String(200),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user_candidate.id'))
    
    
    
    
    

# class Applicants(db.Model):
#     __tablename__ = 'applicants'
#     id=db.Column(db.Integer,primary_key=True)
#     job_id = db.Column(db.String(200),nullable=False)
#     applicant_name = db.Column(db.String(200),nullable=False)
#     applicantion_id = db.Column(db.String(200),nullable=False)
#     applicant_email = db.Column(db.String(200),nullable=False)
#     applicant_resume = db.Column(db.String(200),nullable=False)
#     user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    