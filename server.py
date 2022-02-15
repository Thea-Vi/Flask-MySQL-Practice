from flask import Flask, render_template, url_for, request, redirect, session

from user import User

app = Flask(__name__)

app.secret_key = 'count me in'

# 2
@app.route('/')
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template('index.html', all_users = all_users)


#5
# add 2 routes
# needs form route and POST request route
@app.route('/users/new')
def new_user_form():
    return render_template('new_user.html')

@app.route('/users/create', methods = ['POST'])
def create_user():
    # get data from request
    #7
    User.create(request.form)
    
    return redirect('/')
# to view the added user



if __name__=="__main__":
    app.run(debug=True)
