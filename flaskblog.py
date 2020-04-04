from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app=Flask(__name__)
app.config['SECRET_KEY']='a7fd5acc43d6d9fb0ba3c134db4ae626'
posts = [
    
    {   
        'name':'The Alchemist',
        'author':'Poulo Cohelo',
        'date':'21 April'

    },
      {   
        'name':'The shady',
        'author':'Pula deshpande',
        'date':'25 April'

    }

]

posts2=[
    {
        'name':'Chetan bhagat'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',name_p=posts,title='home')


@app.route("/about")
def about():
    return render_template('about.html',name_p2=posts2,title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form,title='Register')

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',form=form,title='Login')


# if __name__=='__main__':
#     app.run(debug=True)