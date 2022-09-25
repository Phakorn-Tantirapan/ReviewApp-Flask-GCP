from typing import Text
from main import db
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import declarative_base, validates


Base = declarative_base()

class Topics(db.Model):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    ord = Column(String(30), unique=True, nullable=True)
    topic = Column(String(500), unique=False, nullable=False)
    dt = Column(Date, unique=False, nullable=False)
    is_active = Column(Boolean, unique = False, nullable=False, default=True) # True is Active, False is Inactive
    ss = db.relationship('ScoreSurvey', backref='ord')

class ScoreSurvey(db.Model):
    __tablename__ = 'score_survey'
    id = Column(Integer, primary_key=True)
    ord_id = Column(String(30), ForeignKey('topics.ord'))
    overall = Column(Integer, unique = False, nullable=False)
    most_love = Column(String(30), unique = False, nullable=False)
    rpt = Column(Boolean, unique = False, nullable=False) # True is repeat, Flase is not repeat
    cmt = Column(String(1000), unique = False, nullable=True)
