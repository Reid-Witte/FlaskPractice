from flask import Flask, render_template
import datetime
import calendar

app = Flask(__name__)

link = "<link rel=\"stylesheet\" href=\"static/css/main.css\">"

today = datetime.datetime.now()
dayname = calendar.day_name[today.weekday()]
#day = str(today.day)
month = ", "+calendar.month_name[today.month]
date = " "+str(today.day)
year = ' '+str(today.year)
time = " "+str(today.strftime("%X"))

@app.route('/')
def index():
    return link + '\n<h1>The current date time is '+dayname+month+date+year+time+'</h1>' 

if __name__ == "__main__":
    app.run(debug=True)