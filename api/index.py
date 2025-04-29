from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__, static_folder="../static", template_folder="../templates")
CORS(app)

grade_points = {
    'S': 10,
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 0
}

@app.route('/', methods=['GET', 'POST'])
def index():
    gpa = None
    if request.method == 'POST':
        total_points = 0
        total_credits = 0

        for i in range(1, 9):
            grade = request.form.get(f'grade{i}')
            credits = request.form.get(f'credits{i}')

            if grade and credits:
                try:
                    credit_value = int(credits)
                    point_value = grade_points.get(grade.upper(), 0)
                    total_points += credit_value * point_value
                    total_credits += credit_value
                except ValueError:
                    continue

        if total_credits > 0:
            gpa = round(total_points / total_credits, 2)

    return render_template("index.html", gpa=gpa)

if __name__ == '__main__':
    app.run()
