from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [] 

@app.route('/')

def index(): 
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    content = request.form.get('content')
    if content:
        tasks.append({'id': len(tasks) + 1, 'content': content})
    return redirect(url_for('index'))

if __name__ == '__main__': app.run(debug=True)