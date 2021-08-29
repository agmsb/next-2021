from flask import Flask, request, render_template, abort
import os

app = Flask(__name__)
FEATURE = os.environ.get('FEATURE')

@app.route('/')
def hello():
    return render_template('index.html', FEATURE=FEATURE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)