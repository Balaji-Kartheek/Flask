### Integrating with the HTML page
### HTTP verb (GET and POST)

## render_template = used for linking to the HTML page
## request is used to get the information from the Application

from flask import Flask,redirect,url_for,render_template,request     
app=Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/inner/<int:score>')  # creating a sub-directory with a input parameter called marks
def inner(score):
    return "Welcome to Inner Page having a score of "+str(score)


#success page
@app.route('/success/<int:marks>')
def success(marks):
    res=marks
    return render_template('pass.html',result=res)

#fail page
@app.route('/fail/<int:marks>')
def fail(marks):
    res=marks
    return render_template('fail.html',result=res)

### returns the marks of the form input
@app.route('/submit',methods=['POST','GET'])
def results():
    
    if request.method=="POST":
        marks=int(request.form['marks'])
        if(marks<18):
            result="fail"
            
        else:
            result="success"
        return redirect(url_for(result,marks=marks))

if __name__=="__main__":
    app.run(debug=True)