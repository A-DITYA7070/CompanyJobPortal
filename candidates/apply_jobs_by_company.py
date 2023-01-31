from config import db

class Apply_jobs_by_company(db.Model):
    __tablename__ = 'Apply_jobs_by_company'
    name = db.Column(db.String(200),nullable=False)
    company = db.Column(db.String(200),nullable=False)
    company_id =db.Column(db.String(200),nullable=False)
    intern_duration=db.Column(db.String(200),nullable=False)
    ctc_expected = db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.String(200),db.ForeignKey('user.id'))