from flask import Flask
a=Flask("first2")
@a.route("/")
def index():
    return("sucess")
a.run()
