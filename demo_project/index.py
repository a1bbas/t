from flask import Flask,render_template,request,redirect,url_for,session,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "myhello"


# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return f"<User {self.name}>"



@app.route("/")
def home():
    if "username" in session:
        return render_template("index.html",r=session["username"])
    return redirect(url_for("login"))

@app.route("/login",methods=["GET","POST"])
def login():

    if "username" in session:
        return render_template("user.html")
    if request.method == "POST":
            user = request.form["nm"]
            session['username'] = user
            print(f"user {user}")
            flash("You have logged in Successfuly","success")
            return redirect(url_for("user"))

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username",None)
        flash("You have been logged out","info")
        return redirect(url_for("login"))

@app.route("/user")    
def user():
    if "username" in session:
        usr = session["username"]
        return render_template("user.html",user=usr)
    return redirect(url_for("login"))

@app.route("/new")
def test():
    return render_template("new.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)