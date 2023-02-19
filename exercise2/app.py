from flask import Flask, render_template, request, url_for

app = Flask(__name__)

num = 0
link = "<link rel=\"stylesheet\" href=\"static/css/main.css\">"
line1 = "<h1>Home</h1>"
line2 = "<h2>Enter an integer to find out if it is even or odd</h2>"
line3 = "<h3>Number</h4>"
line4 = "<form action=\"\" method=\"post\"><input type=\"text\" id=\"Number\"name=\"Number\"><br><br><input type=\"submit\" value=\"Submit\"></form>"
line5 = ""

@app.route('/', methods=['GET','POST'])
def index():
    data = request.form.get("Number")
    if(data != None):
        result1 = "<h1>Calculate</h1>"
        result2 = ""
        if(type(data) != 'int'):
            result2= "<h2>"+str(data)+" is not a number!</h2>"
        elif(data == ''):
            result2 = "<h2>No number provided!</h2>"
        elif(int(data) % 2 == 0):
            result2 = "<h2>"+str(data)+" is even</h2>"
        else:
            result2 = "<h2>"+str(data)+" is odd</h2>"
        result3 = "<h3><a href= \"\">Go home</a></h4>"
        return link + result1 + result2 + result3
    return link + line1+ line2 + line3 + line4 + line5


if __name__ == "__main__":
    app.run(debug=True)