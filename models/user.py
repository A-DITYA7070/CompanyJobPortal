from config import db 

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(200),nullable=False)
    addDetailsUser=db.relationship('AddDetailsUser',backref='user')
    addDetails = db.relationship('AddDetails',backref='user')
    applyInternships =db.relationship('ApplyInternships',backref='user')
    applyJobsByCompany=db.relationship('ApplyJobsByCompany',backref='user')
    jobsForArmyRetired=db.relationship('JobsForArmyRetired',backref='user')
    jobsForStudents=db.relationship('JobsForStudents',backref='user')
    listCompany=db.relationship('ListCompany',backref='user')
    listJobsForEveryone=db.relationship('ListJobsForEveryone',backref='user')
    manageAppliedJobs=db.relationship('ManageAppliedJobs',backref='user')
    managePostedJobs=db.relationship('ManagePostedJobs',backref='user')
    postInternships=db.relationship('PostInternships',backref='user')
    postJobsAsCompany=db.relationship('PostJobsAsCompany',backref='user')