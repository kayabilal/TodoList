from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/kayab/OneDrive/Masaüstü/TodoApp/todo.db"
db.init_app(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


#index
@app.route("/")
def index(): 
    todos = Todo.query.all()
    return render_template("index.html",todos=todos)

#complete
@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    """
    if todo.complete == True:
        todo.complete = False
    else:
        todo.complete = True
    """
    todo.complete = not todo.complete

    db.session.commit()
    return redirect(url_for("index"))

#add
@app.route("/add",methods = ["POST"])
def addTodo():
    title = request.form.get("title")
    newTodo = Todo(title = title,complete =False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

#delete
@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

"""@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

from flask import flash, redirect, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from my_app import db
from my_app.api.models import User
from my_app.api.forms import RegisterForm, LoginForm

from flask import flash, redirect
from flask_login import login_user,logout_user

todo = Blueprint('tasks', __name__)

@todo.route('/logout', methods = ['POST','GET'])
def logout():
    logout_user()
    return redirect('/home')

@todo.route('/login', methods = ['POST','GET'])
def login():
        form = LoginForm()
        if form.validate_on_submit:
            user = User.query.filter_by(email = form.email.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('/todos')
            flash("Invalid details")
               
        return render_template('login.html', form=form)"""

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
