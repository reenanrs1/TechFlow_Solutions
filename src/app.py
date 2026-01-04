from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [] 

@app.route('/')

def index(): 
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    content = request.form.get('content')
    priority = request.form.get('priority') # Novo campo de prioridade
    if content:
        tasks.append({'id': len(tasks) + 1, 'content': content, 'priority': priority})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    # Busca a tarefa pelo ID
    task = next((t for t in tasks if t['id'] == task_id), None)
    if request.method == 'POST':
        task['content'] = request.form.get('content')
        task['priority'] = request.form.get('priority')
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

if __name__ == '__main__': app.run(debug=True)