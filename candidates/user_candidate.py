from config import db

class User_candidate(db.Model):
    __tablename__ = 'user_candidate'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200),nullable=False)
    add_details = db.relationship('Add_details',backref='user')
    apply_internship = db.relationship('Apply_intership',backref='user')
    apply_jobs_by_company = db.relationship('Apply_jobs_by_company',backref='user')
    jobs_for_army_retired = db.relationship('Jobs_for_army_retired',backref='user')
    manage_applied_jobs = db.relationship('Manage_applied_jobs',backref='apply_jobs_by_company')
    
    
    
    
    
    
    # username = db.Column(db.String(200),nullable=False)
    # applicants = db.relationship('Applicants',backref='user')
    # availablejobs = db.relationship('Availablejobs',backref='user')
    # jobappliedbyuser = db.relationship('Jobappliedbyuser',backref='user')
    # postedjobs = db.relationship('Postedjobs',backref='user')
    