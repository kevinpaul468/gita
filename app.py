from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Chapter, Sloka
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gita.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/chapters', methods=['GET'])
def get_chapters():
    chapters = Chapter.query.all()
    return jsonify([{
        "chapter_name": chapter.chapter_name,
        "chapter_number": chapter.chapter_number,
        "verse_count": chapter.verse_count,
        "language": chapter.language,
        "yoga_name": chapter.yoga_name,
        "meaning": chapter.meaning,
        "summary": chapter.summary
    } for chapter in chapters])

@app.route('/chapters/<language>', methods=['GET'])
def get_chapters_by_language(language):
    chapters = Chapter.query.filter_by(language=language).all()
    return jsonify([{
        "chapter_name": chapter.chapter_name,
        "chapter_number": chapter.chapter_number,
        "verse_count": chapter.verse_count,
        "language": chapter.language,
        "yoga_name": chapter.yoga_name,
        "meaning": chapter.meaning,
        "summary": chapter.summary
    } for chapter in chapters])

@app.route('/chapters/<int:chapter_number>/<language>', methods=['GET'])
def get_chapter_details(chapter_number, language):
    chapter = Chapter.query.filter_by(chapter_number=chapter_number, language=language).first()
    if chapter:
        return jsonify({
            "chapter_name": chapter.chapter_name,
            "chapter_number": chapter.chapter_number,
            "verse_count": chapter.verse_count,
            "language": chapter.language,
            "yoga_name": chapter.yoga_name,
            "meaning": chapter.meaning,
            "summary": chapter.summary
        })
    else:
        return jsonify({"error": "Chapter not found"}), 404

@app.route('/chapters/id/<int:chapter_id>', methods=['GET'])
def get_chapter_by_id(chapter_id):
    chapter = Chapter.query.get(chapter_id)
    if chapter:
        return jsonify({
            "chapter_name": chapter.chapter_name,
            "chapter_number": chapter.chapter_number,
            "verse_count": chapter.verse_count,
            "language": chapter.language,
            "yoga_name": chapter.yoga_name,
            "meaning": chapter.meaning,
            "summary": chapter.summary
        })
    else:
        return jsonify({"error": "Chapter not found"}), 404

@app.route('/chapters/<int:chapter_number>/slokas', methods=['GET'])
def get_total_slokas(chapter_number):
    chapter = Chapter.query.filter_by(chapter_number=chapter_number).first()
    if chapter:
        return jsonify({"total_slokas": chapter.verse_count})
    else:
        return jsonify({"error": "Chapter not found"}), 404

@app.route('/chapters/<int:chapter_number>/slokas/<int:sloka_number>/<language>', methods=['GET'])
def get_sloka_details(chapter_number, sloka_number, language):
    sloka = Sloka.query.filter_by(chapterNumber=chapter_number, slokaNumber=sloka_number, language=language).first()
    if sloka:
        return jsonify({
            "sloka_number": sloka.slokaNumber,
            "chapter_number": sloka.chapterNumber,
            "speaker": sloka.speaker,
            "language": sloka.language,
            "sloka": sloka.sloka,
            "meaning": sloka.meaning
        })
    else:
        return jsonify({"error": "Sloka not found"}), 404



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)