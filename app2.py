from flask import Flask
app=Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to Kartheek Page"

@app.route('/inner/<int:score>')  # creating a sub-directory with a input parameter called score
def inner(score):
    return "Welcome to Inner Page having a score of "+str(score)

@app.route('/results/<int:score>')
def inner(score):
    if(score<18):
        return "Fail"
    else:
        return "Pass"


if __name__=="__main__":
    app.run(debug=True)