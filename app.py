import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/user_login_type', methods=['POST'])
def user_login_type():
    user_role = request.form['userRole']
    
    if user_role == 'Police':
        return redirect(url_for('police_docs_upload'))
    elif user_role == 'Lawyer':
        return redirect(url_for('lawyer_docs_upload'))
    elif user_role == 'Judge':
        return redirect(url_for('judge_docs_upload'))
    elif user_role == 'Courtroom':
        return redirect(url_for('courtroom_docs_upload'))

@app.route('/police-view-fir')
def police_view_fir():
    return render_template('police-view-fir.html')  # Your police upload page

@app.route('/case-video-evidences')
def case_video_evidences():
    return render_template('case-video-evidences.html')  # Your police upload page

@app.route('/police-docs-upload')
def police_docs_upload():
    return render_template('police-docs-upload.html')  # Your police upload page

@app.route('/lawyer-docs-upload')
def lawyer_docs_upload():
    return render_template('lawyer-docs-upload.html')  # Your lawyer upload page

@app.route('/judge-docs-upload')
def judge_docs_upload():
    return render_template('judge-docs-upload.html')  # Your judge upload page

@app.route('/courtroom-docs-upload')
def courtroom_docs_upload():
    return render_template('courtroom-docs-upload.html')  # Your courtroom upload page

    
if __name__ == '__main__':
   app.run()
