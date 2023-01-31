from config import db 
class ApplyJobsByCompany(db.Model):
    __tablename__ = 'applyJobsByCompany'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    company_name = db.Column(db.String(200),nullable=False)
    resume_url=db.Column(db.String(200),nullable=False)
    skills=db.Column(db.String(200),nullable=False)
    role = db.Column(db.String(200),nullable=False)
    ctc_expected=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))