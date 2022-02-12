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
        print(type(image))
        new_image = image_database(Id=image['ID'], label=image['Label'])

        try:
            db.session.add(new_image)
            db.session.commit()
            return redirect("/")
        except:
            return "Image upload error"
    
    else:
        images = image_database.query.order_by(image_database.date_created).all()
        # images = image_database.order_by(image_database.date_created).first() # for recent one
        return render_template('index.html', images=images)
    
    

if __name__ == "__main__":
    app.run(debug=True)