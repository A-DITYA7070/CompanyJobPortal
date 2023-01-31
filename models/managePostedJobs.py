from config import db 
class ManagePostedJobs(db.Model):
    __tablename__ = 'managePostedJobs'
    id=db.Column(db.Integer,primary_key=True)
    add_jobs=db.Column(db.String(200),nullable=False)
    delete_jobs=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))