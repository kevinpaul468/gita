from extensions import db

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapterName = db.Column(db.String(100), nullable=False)
    chapterNumber = db.Column(db.Integer, nullable=False)
    verseCount = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(10), nullable=False)
    yogaName = db.Column(db.String(100), nullable=False)
    meaning = db.Column(db.Text, nullable=True)
    summary = db.Column(db.Text, nullable=True)

class Sloka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slokaNumber = db.Column(db.Integer, nullable=False)
    chapterNumber = db.Column(db.Integer, nullable=False)
    speaker = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(10), nullable=False)
    sloka = db.Column(db.Text, nullable=False)
    meaning = db.Column(db.Text, nullable=True)