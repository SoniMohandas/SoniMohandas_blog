from flask import Flask, render_template, url_for, flash, redirect
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
        'author': 'Harigovind Soni',
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

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful!, Please enter valid username and password', 'danger')            
    return render_template('login.html', title = 'Login', form = form)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

if __name__ == "__main__":    
    app.run(debug = True)