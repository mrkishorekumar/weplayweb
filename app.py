from turtle import heading
from flask import Flask,render_template

import mysql.connector as mysql

db = mysql.connect(host="sql6.freemysqlhosting.net",user="sql6500917",passwd="Xsq4gpvKHi",db="sql6500917")

command_handler = db.cursor(buffered=True)

app = Flask(__name__)

@app.route('/')
def HomePage():
    command_handler.execute("SELECT Heading FROM HomePage")
    records = command_handler.fetchall()   
    home = []
    for i in records:
        for j in i:
            home.append(j)

    command_handler.execute("SELECT Paragraph FROM HomePage")
    records = command_handler.fetchall()   
    paragraph = []
    for i in records:
        for j in i:
            paragraph.append(j)

    return render_template('index.html' ,heading=home ,para=paragraph)    

@app.route('/about')
def AboutPage():
    return render_template('about.html')  

@app.route('/contact')
def ContactPage():
    return render_template('contact.html')  

@app.route('/portfolio')
def PortfolioPage():
    return render_template('portfolio.html')  

@app.route('/service')
def ServicePage():
    return render_template('service.html')  


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
