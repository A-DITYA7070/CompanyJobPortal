from config import db 
class ListCompany(db.Model):
    __tablename__ = 'listCompany'
    id=db.Column(db.Integer,primary_key=True)
    company_name = db.Column(db.String(200),nullable=False)
    location=db.Column(db.String(200),nullable=False)
    no_of_employee=db.Column(db.String(200),nullable=False)
    company_type=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))