from config import db 
class JobsForArmyRetired(db.Model):
    __tablename__ = 'jobsForArmyRetired'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    skills=db.Column(db.String(200),nullable=False)
    role = db.Column(db.String(200),nullable=False)
    army_rank=db.Column(db.String(200),nullable=False)
    salary_expected=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))