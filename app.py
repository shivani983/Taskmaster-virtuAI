from flask import Flask, render_template,url_for,redirect # importing required modules
app= Flask(__name__)  #creating instance for flask app

@app.route("/") #routing for webpage before lgoin or signup
def home():
    return render_template("home.html")
@app.route("/homepage") # routing for homeogae
def homepage():   # function to render homepage
    return render_template("homepage.html")
@app.route('/login', methods=['GET', 'POST']) # routing for login page
def login():
    return render_template('login.html') #rendering login page

@app.route('/signup', methods=['GET', 'POST']) #routing for  page
def signup():
    return render_template('signup.html')    #rendering  page
@app.route("/learnmore")           #routing for login page
def learnmore():
    return render_template("learnmore.html")   #rendering  page
@app.route("/forgotpass",methods=['GET','POST']) #routing for  page
def forgotpass():             
    return render_template("forgotpass.html")  #rendering  page
@app.route("/getstarted",methods=['GET','POST'])
def getstarted():
    return render_template('signup.html')
@app.route("/cancel",methods=['GET'])
def cancel():
    return render_template('cancel.html')



if __name__== "__main__":   #conditional statement bacause in python  the value of the variable(__name__) is string("__main__")
    app.run(host='0.0.0.0' ,debug=True,port=5001) #running the app on port no.=5001 with local host
