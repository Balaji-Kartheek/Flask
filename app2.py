# Building url dynamically

from flask import Flask,redirect,url_for     # req. for url redirection
app=Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to Kartheek Page"

@app.route('/inner/<int:score>')  # creating a sub-directory with a input parameter called marks
def inner(score):
    return "Welcome to Inner Page having a score of "+str(score)


#success page
@app.route('/success/<int:marks>')
def success(marks):
    return "Passed with marks: "+str(marks)

#fail page
@app.route('/fail/<int:marks>')
def fail(marks):
    return "Failed with marks: "+str(marks)


@app.route('/results/<int:marks>')
def inner2(marks):
    result=""
    if(marks<18):
        result="fail"
    else:
        result="success"
    return redirect(url_for(result,marks=marks))   # 2 params


if __name__=="__main__":
    app.run(debug=True)