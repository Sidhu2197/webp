from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Hyderabad',
        'salary': '5 LPA'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bangalore',
        'salary': '10 LPA'
    },
    {
        'id': 3,
        'title': 'Data Engineer',
        'location': 'Mumbai',
        'salary': '8 LPA'
    }
]

@app.route('/')
def home():
    return render_template('p1home.html', jobs=JOBS)

if __name__ == "__main__":
    app.run(debug=True)