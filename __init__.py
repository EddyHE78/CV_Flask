from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)  # Création de l'application Flask

@app.route('/')
def home():
    return redirect(url_for('resume_1'))

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

if __name__ == "__main__":
    app.run()
