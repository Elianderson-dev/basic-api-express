from flask import Flask
app = Flask(__name__)

@app.route("/")
def msg():
    user_msg = input("• Dear user, type a message: ")
    return(user_msg)
    