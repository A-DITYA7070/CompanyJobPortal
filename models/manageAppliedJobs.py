from config import db 
class ManageAppliedJobs(db.Model):
    __tablename__ = 'manageAppliedJobs'
    id=db.Column(db.Integer,primary_key=True)
    delete_applied_job = db.Column(db.String(200),nullable=False)
    add_applied_job=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))