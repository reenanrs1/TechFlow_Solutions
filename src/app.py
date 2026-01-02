from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = [] 
@app.route('/')
def index(): return "TechFlow Ativa"
if __name__ == '__main__': app.run(debug=True)