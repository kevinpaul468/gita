from flask import Flask, request, jsonify
from models import Chapter, Sloka
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gita.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/chapters', methods=['GET'])
def get_chapters():
    chapters = Chapter.query.all()
    return jsonify([{
        "chapterName": chapter.chapterName,
        "chapterNumber": chapter.chapterNumber,
        "verseCount": chapter.verseCount,
        "language": chapter.language,
        "yogaName": chapter.yogaName,
        "meaning": chapter.meaning,
        "summary": chapter.summary
    } for chapter in chapters])

@app.route('/chapters/<language>', methods=['GET'])
def get_chapters_by_language(language):
    chapters = Chapter.query.filter_by(language=language).all()
    return jsonify([{
        "chapterName": chapter.chapterName,
        "chapterNumber": chapter.chapterNumber,
        "verseCount": chapter.verseCount,
        "language": chapter.language,
        "yogaName": chapter.yogaName,
        "meaning": chapter.meaning,
        "summary": chapter.summary
    } for chapter in chapters])

@app.route('/chapters/<int:chapterNumber>/<language>', methods=['GET'])
def get_chapter_details(chapterNumber, language):
    chapter = Chapter.query.filter_by(chapterNumber=chapterNumber, language=language).first()
    if chapter:
        return jsonify({
            "chapterName": chapter.chapterName,
            "chapterNumber": chapter.chapterNumber,
            "verseCount": chapter.verseCount,
            "language": chapter.language,
            "yogaName": chapter.yogaName,
            "meaning": chapter.meaning,
            "summary": chapter.summary
        })
    else:
        return jsonify({"error": "Chapter not found"}), 404

@app.route('/chapters/id/<int:chapterId>', methods=['GET'])
def get_chapter_by_id(chapterId):
    chapter = Chapter.query.get(chapterId)
    if chapter:
        return jsonify({
            "chapterName": chapter.chapterName,
            "chapterNumber": chapter.chapterNumber,
            "verseCount": chapter.verseCount,
            "language": chapter.language,
            "yogaName": chapter.yogaName,
            "meaning": chapter.meaning,
            "summary": chapter.summary
        })
    else:
        return jsonify({"error": "Chapter not found"}), 404
    
    
@app.route('/chapters/<int:chapterNumber>/slokas', methods=['GET'])
def get_total_slokas(chapterNumber):
    chapter = Chapter.query.filter_by(chapterNumber=chapterNumber).first()
    if chapter:
        return jsonify({"totalSlokas": chapter.verseCount})
    else:
        return jsonify({"error": "Chapter not found"}), 404

@app.route('/chapters/<int:chapterNumber>/slokas/<int:slokaNumber>/<language>', methods=['GET'])
def get_sloka_details(chapterNumber, slokaNumber, language):
    sloka = Sloka.query.filter_by(chapterNumber=chapterNumber, slokaNumber=slokaNumber, language=language).first()
    if sloka:
        return jsonify({
            "slokaNumber": sloka.slokaNumber,
            "chapterNumber": sloka.chapterNumber,
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