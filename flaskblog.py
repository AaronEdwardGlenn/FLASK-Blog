from forms import RegistrationForm, LoginForm
from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)

app.config['SECRET_KEY'] = '4168461357cf940173596c551cc9ea6d'

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


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
