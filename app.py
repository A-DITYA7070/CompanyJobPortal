from flask import Flask, request,jsonify
from flask_cors import CORS
from config import db,SECRET_KEY
from os import path,getcwd,environ
from dotenv import load_dotenv
from models.user import User
from models.addDetails import AddDetails
from models.applyInternships import ApplyInternships
from models.applyJobsByCompany import ApplyJobsByCompany
from models.jobsForArmyRetired import JobsForArmyRetired
from models.jobsForStudents import JobsForStudents
from models.listCompany import ListCompany
from models.listJobsForEveryone import ListJobsForEveryone
from models.manageAppliedJobs import ManageAppliedJobs
from models.managePostedJobs import ManagePostedJobs
from models.postInternships import PostInternships
from models.postJobsAsCompany import PostJobsAsCompany
from models.addDetailsUser import AddDetailsUser

load_dotenv(path.join(getcwd(),'.env'))

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SQLALCHEMY_ECHO']=False
    app.secret_key = SECRET_KEY
    
    db.init_app(app)
    print("DB Initialized successfully..")
    with app.app_context():
        @app.route("/signup",methods=['POST'])
        def signup():
            data = request.form.to_dict(flat=True)
            new_user = User(
                username=data['username']
            )
            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg="user added successfully..")
        
        @app.route("/add_user_details",methods=['POST'])
        def add_user_details():
            data=request.get_json()
            username = request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=AddDetailsUser(
                name=data['name'],
                email_id=data['email_id'],
                resume_url=data['resume_url'],
                skills = data['skills'],
                age_group = data['age_group'],
                jobs_applied=data['jobs_applied'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="user details added..")
        
        @app.route("/apply_internships",methods=['POST'])
        def apply_internships():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=ApplyInternships(
                name=data['name'],
                company=data['company'],
                resume_url=data['resume_url'],
                skills=data['skills'],
                role=data['role'],
                internduration=data['internduration'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(data='internship applied successfully..')
        
        @app.route("/apply_jobs_by_company",methods=['POST'])
        def apply_jobs_by_company():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=ApplyJobsByCompany(
                name=data['name'],
                company_name=data['company_name'],
                resume_url=data['resume_url'],
                skills=data['skills'],
                role=data['role'],
                ctc_expected=data['ctc_expected'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="jobs applied...")
        
        @app.route("/jobs_for_retired_army",methods=['POST'])
        def jobs_for_retired_army():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=JobsForArmyRetired(
                name=data['name'],
                skills=data['skills'],
                role=data['role'],
                army_rank=data['army_rank'],
                salary_expected=data['salary_expected'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="jobs applied...")
        
        @app.route("/jobs_for_students",methods=['POST'])
        def jobs_for_students():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=JobsForStudents(
                name=data['name'],
                job_desc=data['job_desc'],
                salary_expected=data['salary_expected'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="students jobs applied..")
        
        @app.route('/list_your_company',methods=['POST'])
        def list_your_company():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=ListCompany(
                company_name=data['company_name'],
                location=data['location'],
                no_of_employee=data['no_of_employee'],
                company_type=data['company_type'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg=f"successfully listed company.. {data['company_name']}")
            
        @app.route('/list_job_for_everyone',methods=['POST'])
        def list_job_for_everyone():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=ListJobsForEveryone(
                name=data['name'],
                company_name=data['company_name'],
                skills=data['skills'],
                job_desc=data['job_desc'],
                role=data['role'],
                salary_expected=data['salary_expected'],
                job_type=data['job_type'],
                user_id=user.id 
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(data="jobs_listed...")
            
        @app.route('/manage_applied_jobs',methods=['POST'])
        def manage_applied_jobs():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=ManageAppliedJobs(
                delete_applied_job=data['deleted_jobs'],
                add_applied_job = data['add_applied_job'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="updated..")
        
        @app.route('/manage_posted_jobs',methods=['POST'])
        def manage_posted_jobs():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=ManagePostedJobs(
                add_jobs=data['add_jobs'],
                delete_jobs=data['delete_jobs'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="updated..")
        
        @app.route('/post_internships',methods=['POST'])
        def post_internships():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=PostInternships(
                company_name=data['company_name'],
                intern_type=data['intern_type'],
                location=data['location'],
                resume_url=data['resume_url'],
                skills=data['skills'],
                role=data['role'],
                salary_expected=data['salary_expected'],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="internships posted..")
            
        @app.route('/post_jobs_as_company',methods=['POST'])
        def post_jobs_as_company():
            data=request.get_json()
            username=request.args.get('username')
            user=User.query.filter_by(username=username).first()
            user_details=PostJobsAsCompany(
                company_name=data["company_name"],
                job_type=data["job_type"],
                resume_url=data["resume_url"],
                skills_required=data["skills_required"],
                role=data["role"],
                ctc_offered=data["ctc_offered"],
                job_desc=data["job_desc"],
                location=data["location"],
                user_id=user.id
            )
            db.session.add(user_details)
            db.session.commit()
            return jsonify(msg="posted job as company..")   
        
    
        # db.drop_all()
        db.create_all()
        db.session.commit()
        return app
    
if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)
