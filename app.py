from flask import Flask, render_template, request

app = Flask(__name__)

# Mapping of Grades to Points
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

        for i in range(1, 9):  # 8 subjects assumed
            grade = request.form.get(f'grade{i}')
            credit = request.form.get(f'credit{i}')

            if grade and credit:
                try:
                    credit_value = int(credit)
                    point_value = int(grade)
                    total_points += credit_value * point_value
                    total_credits += credit_value
                except ValueError:
                    continue

        if total_credits > 0:
            gpa = round(total_points / total_credits, 2)

    return render_template('index.html', gpa=gpa)

if __name__ == '__main__':
    app.run(debug=True)
