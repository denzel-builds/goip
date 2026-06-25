from app.database import SessionLocal
from app.models.opportunity import Opportunity
from datetime import date

db = SessionLocal()

opportunities_data = [
    {"title": "Software Engineering Graduate Programme", "company": "BBD", "type": "graduate", "location": "Johannesburg", "deadline": date(2026, 8, 31), "url": "https://bbdsoftware.com/grad"},
    {"title": "Entelect Graduate Programme", "company": "Entelect", "type": "graduate", "location": "Pretoria", "deadline": date(2026, 9, 15), "url": "https://entelect.co.za/grad"},
    {"title": "IT Summer Internship", "company": "Absa", "type": "internship", "location": "Sandton", "deadline": date(2026, 10, 1), "url": "https://absa.co.za/careers"},
    {"title": "Tech Graduate Trainee", "company": "Standard Bank", "type": "graduate", "location": "Rosebank", "deadline": date(2026, 7, 30), "url": "https://standardbank.co.za/careers"},
    {"title": "Quant & Tech Learner", "company": "Nedbank", "type": "learnership", "location": "Sandton", "deadline": date(2026, 11, 15), "url": "https://nedbank.co.za/careers"},
    {"title": "Junior Python Developer", "company": "Boxfusion", "type": "internship", "location": "Centurion", "deadline": date(2026, 6, 30), "url": "https://boxfusion.co.za/careers"},
    {"title": "Data Engineering Bursary", "company": "FNB", "type": "bursary", "location": "Johannesburg", "deadline": date(2026, 10, 30), "url": "https://fnb.co.za/careers"},
    {"title": "Tech Consulting Graduate", "company": "Deloitte", "type": "graduate", "location": "Waterfall", "deadline": date(2026, 8, 15), "url": "https://deloitte.com/za/careers"},
    {"title": "Cybersecurity Internship", "company": "PwC", "type": "internship", "location": "Midrand", "deadline": date(2026, 9, 1), "url": "https://pwc.co.za/careers"},
    {"title": "Backend Dev Graduate", "company": "Capitec", "type": "graduate", "location": "Stellenbosch", "deadline": date(2026, 12, 1), "url": "https://capitecbank.co.za/careers"}
]

for opp in opportunities_data:
    new_opp = Opportunity(**opp)
    db.add(new_opp)

db.commit()
print("Successfully seeded 10 SA tech opportunities!")
db.close()