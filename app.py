from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == "__main__":    
    app.run(debug = True)