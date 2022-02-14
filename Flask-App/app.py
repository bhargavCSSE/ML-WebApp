from cProfile import label
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/CIFAR-10.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class image_database(db.Model):
    Id = db.Column('ID' ,db.Integer, primary_key=True)
    label = db.Column('Label',db.String(200), nullable=False)
    date_created = db.Column('Date', db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<ID %r>' % self.id, '<Label %r>' % self.label

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        image = request.form.to_dict()
        new_image = image_database(Id=image['ID'], label=image['Label'])

        try:
            db.session.add(new_image)
            db.session.commit()
            return redirect("/")
        except:
            return "Error 1: Image upload error"
    
    else:
        images = image_database.query.order_by(image_database.date_created).all()
        return render_template('index.html', images=images)

@app.route('/delete/<int:Id>')
def delete(Id):
    image_to_delete = image_database.query.get_or_404(Id)

    try:
        db.session.delete(image_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Error 2: Image delete error"

@app.route('/update/<int:Id>', methods=['GET', 'POST'])
def update(Id):
    image = image_database.query.get_or_404(Id)

    if request.method == 'POST':
        image.Id = request.form['ID']
        image.label = request.form['Label']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Error-3: Image update error"
    else:
        return render_template('update.html', image=image)

if __name__ == "__main__":
    app.run(debug=True)