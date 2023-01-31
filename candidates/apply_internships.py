from config import db

class Apply_internships(db.Model):
    __tablename__ = 'apply_internships'
    name = db.Column(db.String(200),nullable=False)
    company = db.Column(db.String(200),nullable=False)
    company_id =db.Column(db.String(200),nullable=False)
    intern_duration=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.String(200),db.ForeignKey('user.id'))
    
    