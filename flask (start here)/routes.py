from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    html_response = "<h1 style='color:red;'>Hello World! </h1>"
    return html_response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
