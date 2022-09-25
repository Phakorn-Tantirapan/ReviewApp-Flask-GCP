from pickle import GET
from flask import Flask, request, render_template, session, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from connect_sqlalchemy import connect_by_sqlalchemy, connect_by_unix

app = Flask(__name__)

env = os.environ["CURRENT_ENV"]

if env=='GCP-PRODUCTION' or env=='GCP-PRODUCTION':
    db = SQLAlchemy(connect_by_unix(app))

elif env=='LOCAL':
    db = SQLAlchemy(connect_by_sqlalchemy(app))

else:
    print("Variable was not set!!")

from models import *

@app.route('/')
def roche():
    return redirect(url_for('thankyou'))

@app.route('/<ord_no>', methods=['POST'])

def ord(ord_no):
    topic_ord = Topics.query.filter_by(ord=ord_no).first()
    datedate = topic_ord.dt
    ord_chk = topic_ord.is_active
    if ord_chk == False:
        return redirect(url_for('thankyou'))
    else:
        topic_msg = topic_ord.topic

        if request.method == "POST":
            session['overall_score'] = int(request.form.get('rating_sat'))
            session['repeat_choices'] = bool(request.form.get('repeat'))
            session['comment_text'] = request.form.get('comment')

            if session['overall_score'] == 1 or session['overall_score'] == 2:
                session['most_love'] = request.form.get('most-impress-1')   
            elif session['overall_score'] == 3:
                session['most_love'] = request.form.get('most-impress-2')   
            elif session['overall_score'] == 4 or session['overall_score'] == 5:
                session['most_love'] = request.form.get('most-impress-3')  

            survey_score = ScoreSurvey(
                ord_id=ord_no,
                overall=session.get('overall_score'),
                most_love=session.get('most_love'),
                rpt=session.get('repeat_choices'),
                cmt=session.get('comment_text')
            )


            db.session.add(survey_score)
            db.session.commit()

            new_topic = Topics.query.filter_by(ord=ord_no).first()
            new_topic.is_active = False
            db.session.commit()

            
            return redirect(url_for('thankyou'))


    return render_template('ord.html', topic_msg=topic_msg, ord_no=ord_no, datedate=datedate)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
    

if __name__ == '__main__':
    # app.reload = True
    app.debug = True
    app.run()