from flask import Flask, render_template, url_for, flash, redirect           #import Flask class
from forms import RegistrationForm, LoginForm
app = Flask(__name__)              #__name__: a special name variable, is a name of module; equal "__main__"

app.config['SECRET_KEY'] = '9bafe06174e1bce2da5f8f6c2c12e705'

posts = [
    {
        'author': 'Tienshawn',
        'title': 'Blog 1',
        'content': 'First post',
        'date_posted': 'April 29, 2024',
    },
    {
        'author': 'Jane',
        'title': 'Blog 2',
        'content': 'Second post',
        'date_posted': 'April 30, 2024',
    }
]


@app.route("/")                    #route: what we type in browser to get to a url; "/" is the root page
@app.route("/home")  
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")                    
def about():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'a@gmail.com' and form.password.data == 'a':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title='Register', form=form)

# run the script normally without flask run
if __name__ == '__main__':    # __name__ = __main__ if run the script directly
    app.run(debug=True)




