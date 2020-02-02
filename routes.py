from flask import render_template, url_for, flash, request, redirect, jsonify
from Main.forms import findCandidate
from Main import app
from Main.matchPercentage import match
from Main.speechToText import speech_to_text


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
  job_post_result = request.form['job_post_result']
  if(request.form['vs']=='hi'):
      job_post_result=speech_to_text()

  #pass job_post to obtain keywords and key people
  results, skills = match(job_post_result)
  if filter_result and job_post_result:
      return jsonify({'job_post':job_post_result , 'results':results, "skills":skills})
  return jsonify({'error' : 'Missing data!'})
