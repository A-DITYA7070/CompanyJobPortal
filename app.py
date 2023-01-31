from flask import Flask, request,jsonify
from flask_cors import CORS
from config import db,SECRET_KEY
from os import path,getcwd,environ
from dotenv import load_dotenv
from candidates.add_details import Add_details
from candidates.user_candidate import User_candidate


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
            new_user = User_candidate(
               username=data["username"]
            )
            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg="user added successfully..")
        
       
        db.create_all()
        db.session.commit()
        return app    
            
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)           
            
            
            
            
            
            
            
            