from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Aaron Glenn',
        'title': 'Blog 2',
        'content': 'First Content',
        'date_posted': 'April 28, 2020'
    },
    {
        'author': 'Aaron Edward',
        'title': 'Blog 2',
        'content': 'Second Content',
        'date_posted': 'April 28, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
