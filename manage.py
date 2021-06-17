from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_genre = db.Column(db.String(100), nullable=False)
    date_genre = db.Column(db.DateTime, default=datetime.utcnow)
    name_movie = db.Column(db.String, nullable=False)
    id_movie = db.Column(db.Integer, nullable=False)
     
    def __repr__(self):
        return  '<Genre %r>' % self.id
    
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)