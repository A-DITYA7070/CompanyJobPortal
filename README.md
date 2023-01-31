# Different end Points required for the App

# Candidate App..

User
- /signuplogin
- /add_user_details methods=['POST']
      Name
      email_id
      Password
      Resume_profile
      Jobs Applied
      age-group

- /Get_available_jobs_details methods=['GET']
      {
        "result":[
            {
                "company_name":"Microsoft",
                "job-id":"job.id",
                "company type":"Software",
                "role":"backend developer",
                "description":"develope backend and write apis",
                "location":"banglore",
                "ctc offered":"12lpa",
                "skills required":"c++,python,java,backend"
            },
            {
                "company_name":"google",
                "job-id":"job.id",
                "company type":"Software",
                "role":"backend developer",
                "description":"develope backend and write apis",
                "location":"banglore",
                "ctc offered":"12lpa",
                "skills required":"c++,python,java,backend"
            }
        ]
      }
      

- /Apply_jobs_by_company methods=['POST']
    name
    username
    resume
    job-id
    company name
    ctc expected..
    {
        "msg":"applied successfully"
    }
      
- /Recommended_jobs methods=['GET]
    name
    username
    {
        "msg":[
            {
                "company-name":"Grihatech",
                "job-id":"12",
                "job-type":"full time",
                "salary-offering":"30k/month",
                "job-desc":"website developer",
                "role":"website developer"
            },
             {
                "company-name":"Grihatech",
                "job-id":"12",
                "job-type":"full-time",
                "salary-offering":"30k/month",
                "job-desc":"website developer",
                "role":"website developer"
            }
        ]
    }

- /Apply_for_internships methods=['POST']
   name
   username
   company
   resume
   job-id
   salary expected
   intern duration
   {
    msg:"applied successfully"
   }
    
- /jobs_for_retired_army_personnel methods=['POST']
   name
   username
   job-id
   army-rank
   {
    msg:"applied successfully"
   }

- /jobs_for_students methods=['POST']
  name
  username
  resume
  job-id
  {
    msg:"applied successfully"
  }

  - /your_applied_jobs methods=['GET']
  name
  username
  {
    msg:[
        {
            company-name:"msf",
            "job-id":"1",
            company-type:"software",
            "job-desc":"developer",
            "location":"banglore"
        },
        {
             company-name:"msf",
            "job-id":"1",
            company-type:"software",
            "job-desc":"developer",
            "location":"banglore"
        }
    ]
  }

- /get_total_jobs_applied methods=['GET']
  username
  {
    msg:"5"
  }
- /manage_your_applied_jobs methods=['POST']
  username
  delete_applied_job
  update_applied_job
  add_job

# Company APP

- /signup/login
   username
   password

- /list_your_company methods=['POST']
   company-name
   username
   company-type
   location
   no-of-employees
   {
    msg:"company listed"
   }

- /list_jobs_for_everyone methods=['POST']
   name
   username
   job-type
   job-desc
   salary-offering
   skills-required
   {
    msg:[
        {
            name:"narayan murti",
            username:user.id,
            job-type:"guard",
            "job-desc":"required retired army personnel as homeguard",
            "salary-offered":"30k/month",
            "skills-required":"well desciplined"
        },
        {
            name:"narayan murti",
            username:user.id,
            job-type:"sweeper",
            "job-desc":"required lady sweeper personnel",
            "salary-offered":"30k/month",
            "skills-required":"experienced sweeper"
        },
        { 
            name:"narayan murti",
            username:user.id,
            job-type:"sweeper",
            "job-desc":"required gardener",
            "salary-offered":"30k/month",
            "skills-required":"knowledge of flowers"
        }
    ]
   }

- /post_jobs_as_company methods=['POST']
   company-name
   username
   role
   job-type
   job-desc
   location
   ctc offered
   skills required
   {
    "data":[
        {
            company-name - 'msf',
            username - "micro",
            role - "backend",
            job-type - "full time",
            job-desc - "create api",
            location - "banglore",
            ctc offered - "12lpa",
            skills required - [python,api,backend]
        }
    ]
   }

   {
    "msg":"jobs posted"
   }

- /Hire_Interns methods=['POST']
   company-name
   username
   role
   skills-required
   salary
   location
   remote
   {
    msg:"posted"
   }

- /shortlist_resume methods=['GET']
   username
   {
    msg:[
        {
            "name":"aditya raj",
            "resume:{}
        },{
            "name":"raj",
            "resume":{}
        }
    ]
   }

- /get_posted_job_details methods=['GET']
   username
   {
    postedJobs:{
        [
            {
            company-name - 'msf',
            username - "micro",
            role - "backend",
            job-type - "full time",
            job-desc - "create api",
            location - "banglore",
            ctc offered - "12lpa",
            skills required - [python,api,backend]
            },
            {
            company-name - 'msf',
            username - "micro",
            role - "backend",
            job-type - "full time",
            job-desc - "create api",
            location - "banglore",
            ctc offered - "12lpa",
            skills required - [python,api,backend]
            }
        ]
    }
}

- /Manage_jobs methods=['POST']
  update_jobs
  add_jobs
  delete_jobs
  {
    msg:"updated"
  }