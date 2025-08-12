from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from routes.user import user_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
app.secret_key = 'abc123'

# definindo modelo de dados
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(100), unique=True, nullable=False)


# @app.route('/')
# def root():
#     return '<h1>pagina inicial</h1>'


# registrando o blueprint
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(auth_bp, url_prefix='/auth')

# cRud - read
@app.route('/todo')
def root():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)

# Crud
@app.route('/create', methods=["POST"])
def create_task():
    description = request.form['description']

    # valida se a task ja foi cadastrada
    exists_task = Tasks.query.filter_by(description = description).first()
    if(exists_task):
        return 'Error: repeted task.', 400

    new_task = Tasks(description = description)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

# cruD
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Tasks.query.get(task_id)

    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/')


# crUd
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Tasks.query.get(task_id)

    if task:
        task.description = request.form['description']
        db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5153)