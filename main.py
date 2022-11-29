from flask import *
from flask_mail import Mail,Message
from random import *

app=Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='suganyav459@gmail.com'
app.config['MAIL_PASSWORD']='9597300361'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

otp=randint(00000,99999)

@app.route('/')
def home():

    return render_template("index.html")

@app.route('/verify',methods=['POST'])

def verify():
    email=request.form['email']
    print("email Id :",email)

    msg=Message("OTP ",sender='suganyav459@gmail.com',recipients=[email])
    msg.body=str(otp)
    print(msg.body)
    mail.send(msg)
    print("mail sent to your mailid")
    return render_template('verify.html')

@app.route('/validation',methods=['POST'])


def validation():
    user_otp=request.form['otptxt']

    if otp==int(user_otp):
        return "<h2> mail verified successfully</h2>"
    else:
        return "<h2> Mail not verified again give your email id</h2>",render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)

