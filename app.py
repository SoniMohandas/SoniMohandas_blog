from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bafca2c41f1e3d5d71a8971d9bad2e53'

posts = [
    {
        'author': 'Soni Mohandas',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts, title='Home')

@app.route("/about")
def about():
    return render_template('about.html',posts = posts, title = 'About')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

if __name__ == "__main__":    
    app.run(debug = True)