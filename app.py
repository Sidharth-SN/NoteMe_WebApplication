from datetime import datetime
from flask import Flask, render_template,  request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Notes(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_creat = db.Column(db.Integer, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f'{self.sno} - {self.title}'

@app.route('/', methods = ['GET', 'POST'])
def Home_page():
    if request.method == 'POST':
        n = Notes(title = request.form['title'], desc = request.form['desc'])
        db.session.add(n)
        db.session.commit()
    allnotes = Notes.query.all()
    
    return render_template('index.html', allnotes = allnotes)


@app.route('/update/<int:sno>', methods = ['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        note = Notes.query.filter_by(sno=sno).first()
        note.title = request.form['title']
        note.desc = request.form['desc']
        db.session.add(note)
        db.session.commit()
        return redirect('/')

    note = Notes.query.filter_by(sno=sno).first()
    return render_template('update.html', note = note)


@app.route('/delete/<int:sno>')
def delete(sno):
    note = Notes.query.filter_by(sno=sno).first()
    db.session.delete(note)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
#     put debug = True for showing errors in the browser
    app.run(port = 8080)
