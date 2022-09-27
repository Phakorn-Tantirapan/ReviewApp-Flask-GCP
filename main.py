from pickle import GET
from flask import Flask, request, render_template, session, redirect, url_for, flash
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

@app.route('/<ord_no>', methods=['GET','POST'])

def ord(ord_no):
    topic_ord = Topics.query.filter_by(ord=ord_no).first()
    if topic_ord is None:
        return redirect(url_for('thankyou'))
    else:
        datedate = topic_ord.dt
        ord_chk = topic_ord.is_active
        if ord_chk == False:
            return redirect(url_for('thankyou'))
        else:
            topic_msg = topic_ord.topic
            if request.method == "POST":
                if request.form['submit-button'] == 'SUBMIT' and request.form.get('rating_sat') is not None:
                    overall_score = request.form.get('rating_sat')
                    repeat_choice = request.form.get('repeat')
                    comment_text = request.form.get('comment')
                    most_impress_1 = request.form.get('most-impress-1')
                    most_impress_2 = request.form.get('most-impress-2')
                    most_impress_3 = request.form.get('most-impress-3')

                    session['overall_score'] = overall_score
                    session['repeat_choice'] = repeat_choice
                    session['comment_text'] = comment_text

                    if overall_score == '1' or overall_score == '2':
                        most_love = most_impress_1  
                    elif overall_score == '3':
                        most_love = most_impress_2 
                    elif overall_score == '4' or overall_score == '5':
                        most_love = most_impress_3
                    
                    session['most_love'] = most_love

                    if overall_score is not None and repeat_choice is not None and most_love is not None:
                        survey_score = ScoreSurvey(
                                ord_id=ord_no,
                                overall=int(session.get('overall_score')),
                                most_love=session.get('most_love'),
                                rpt=bool(int(session.get('repeat_choice'))),
                                cmt=session.get('comment_text')
                            )

                        db.session.add(survey_score)
                        db.session.commit()

                        new_topic = Topics.query.filter_by(ord=ord_no).first()
                        new_topic.is_active = False
                        db.session.commit()
                        return redirect(url_for('thankyou'))
                    else:
                        flash('กรุณากรอกข้อมูลในหัวข้อที่มี (*)')
                else:
                    flash('กรุณากรอกข้อมูลในหัวข้อที่มี (*)')

    return render_template('ord.html', topic_msg=topic_msg, ord_no=ord_no, datedate=datedate)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
    

if __name__ == '__main__':
    # app.reload = True
    app.debug = True
    app.run()