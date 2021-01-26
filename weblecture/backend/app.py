from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello Ro /h3>" 
    html = "<h3>Class 16CT /h3>" 
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)