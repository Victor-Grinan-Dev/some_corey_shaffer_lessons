from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'el moro',
        'title': 'bajanda',
        'content': 'bullshit',
        'date': '2009'
    },
    {
        'author': 'vitisman',
        'title': 'el gato',
        'content': 'bullshit 2',
        'date': '2008'
    }
]


@app.route("/")
@app.route("/Home")
def hello():
    return render_template('Home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

# r"C:\Users\victo\PycharmProjects\Autoestudio\Corey_Shafer"
#
# from the
# set FLASK_APP=learn_flask.py
# set FLASK_DEBUG=1
