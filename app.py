from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app configurations
app = Flask(__name__)
# must database settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Task Table/Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Task %r>' % self.title


# Routes
@app.route('/')
def index():
    # Create a new task
    new_task = Task(title='Buy groceries', description='Milk, bread, eggs')
    db.session.add(new_task)
    db.session.commit()

    # Get all tasks from the database
    tasks = Task.query.all()
    print(tasks)
    return render_template('result.html', tasks=tasks)