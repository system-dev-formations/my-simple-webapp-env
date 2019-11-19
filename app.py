import os
from flask import Flask
from flask import render_template
app = Flask(__name__,template_folder='/templates')

color = os.environ.get('APP_COLOR')


@app.route("/")
def main():
    print(color)
    return render_template('hello.html',color=color)

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run()
