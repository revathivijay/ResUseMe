from flask import render_template, url_for, flash, request, redirect
from Main.forms import findCandidate
from Main import app
from Main.scraping import scraper


@app.route('/home', methods=['GET', 'POST'])
def home():
    form = findCandidate()
    if form.validate_on_submit():
        print('Form submitted')
        job_post = form.job_post.data
        results = scraper(job_post)
        print('reached here')
        print(results[1])
    return render_template('resume_home.html',form=form)



