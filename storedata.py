import json
from app import db, app
from models import Sloka, Chapter

with open('./genai.sloka.json', 'r') as file:
    slokas_data = json.load(file)


with app.app_context():

    db.create_all()

    for sloka in slokas_data:
        new_sloka = Sloka(
            slokaNumber=sloka['slokaNumber'],
            chapterNumber=sloka['chapterNumber'],
            speaker=sloka['speaker'],
            language=sloka['language'],
            sloka=sloka['sloka'],
            meaning=sloka['meaning']
        )
        db.session.add(new_sloka)

    db.session.commit()


with open('./genai.chapter.json', 'r') as file:
    chapters_data = json.load(file)

with app.app_context():
    for chapter in chapters_data:
        new_chapter = Chapter(
            chapterName=chapter['chapterName'],
            chapterNumber=chapter['chapterNumber'],
            verseCount=chapter['verseCount'],
            language=chapter['language'],
            yogaName=chapter['yogaName'],
            meaning=chapter['meaning'],
            summary=chapter['summary']
        )
        db.session.add(new_chapter)

    db.session.commit()