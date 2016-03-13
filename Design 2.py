from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('us.html')

@app.route('/us')
def us():
    return render_template('us.html')


@app.route('/world')
def world():
    return render_template('world.html')


@app.route('/illinois')
def illinois():
    return render_template('illinois.html')
    #return render_template('test.html')


if __name__ == '__main__':
    app.run()
