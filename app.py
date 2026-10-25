from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    student_name = "Вероника Федулова"
    return render_template('index.html', name=student_name)

if __name__ == '__main__':
    app.run(debug=True)