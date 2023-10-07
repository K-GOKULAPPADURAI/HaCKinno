from flask import Flask, render_template

app = Flask(__name__)

# Define routes and views
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problem_statement')
def problem_statement():
    return render_template('problem_statement.html')

if __name__ == '__main__':
    app.run(debug=True)
