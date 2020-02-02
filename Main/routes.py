from flask import render_template, url_for, flash, request, redirect, jsonify
from Main.forms import findCandidate
from Main import app


skilldict = {
  "Web Dev": ["HTML","JavaScript","CSS"],
  "Android Dev": ["Java","XML","OOP","Android Studio"],
  "Fashion Designer": ["Fashion","Design","Style"]
}

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = findCandidate()
    print('hi')
    if form.validate_on_submit():
        print('Form submitted')
        job_post = form.job_post.data
        print('reached here')
    return render_template('resume_home.html',form=form)

@app.route('/temp', methods=['POST', 'GET'])
def temp():
  filter_result = request.form['filter_name']
  job_post_result = request.form['job_post_name']
  
  if filter_result and job_post_result:
      if job_post_result in skilldict:
          return jsonify({'job_post':job_post_result , 'filter':filter_result, 'skills':skilldict.get(job_post_result, "oops")})
      return jsonify({'job_post':job_post_result , 'filter':filter_result})
  return jsonify({'error' : 'Missing data!'})


    



