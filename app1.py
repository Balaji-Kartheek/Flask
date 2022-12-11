# First Flask Application


from flask import Flask
app=Flask(__name__)      # creating a object for Flask called "app"


@app.route('/')   # helps to route the application
# Adding Functionalities to our Application
def welcome():
    return "Welcome to Kartheek Page"


if __name__=="__main__":
    app.run()    # by running this file it generates a link in terminal click that.