# src/api/app.py
from flask import Flask, jsonify
from datetime import datetime
from pygit2 import Repository

app = Flask(__name__)

def get_current_branch_name():
    """
    Gets the name of the active Git branch as a string.
    """
    repo = Repository('.').head.shorthand
    return str(repo)

# print(get_current_branch_name())
# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Sample resume content
resume_content = {
    "name": "Eshaan Rathi",
    "email": "erathi@scu.edu",
    "education": "MS in Computer Science",
    "experience": "Software Engineer with 200 years of experience in building SAAS products",
    # more resume content fields go here
}

# Get resume content endpoint
@app.route('/resume', methods=['GET'])
def get_resume():
    resume_content_with_metadata = {
        "resume": resume_content,
        "git_branch": get_current_branch_name(),
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return jsonify(resume_content_with_metadata)

if __name__ == '__main__':
    app.run()


# from flask import Flask

# app = Flask(__name__)

# @app.route("/testing")
# def testing():
#     return "testing"

# if __name__=="__main__":
#     app.run()