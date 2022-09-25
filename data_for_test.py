from typing import OrderedDict
from main import db, Topics, ScoreSurvey
from datetime import date

db.drop_all()
db.create_all()

ord1 = Topics(ord='ord-001', topic='เครื่อง 6800 processing module error', dt=date(2022, 10, 13), is_active=True)
ord2 = Topics(ord='ord-002', topic='เครื่อง c111 tip หัก', dt=date(2022, 2, 14), is_active=True)
ord3 = Topics(ord='ord-003', topic='เครื่อง P471 alignment เพี้ยน', dt=date(2022, 1, 24), is_active=False)
ord4 = Topics(ord='ord-004', topic='เครื่อง CAP consumable handing error', dt=date(2022, 5, 16), is_active=True)

# score1 = ScoreSurvey(ord_id='ord-001', stfy=3, fst=4, expt=5, rpt=True, cmt='เครื่องเสียบ่อย อยากให้ช่างเข้าทุกวันเลย')

db.session.add_all([ord1, ord2, ord3, ord4])
db.session.commit()