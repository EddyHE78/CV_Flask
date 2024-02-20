from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route pour afficher la page resume_1.html
@app.route('/resume_1')
def resume_1():
    # Récupérer les données du CV depuis la base de données ou un fichier
    cv_data = {
        'name': 'John Doe',
        'email': 'john@example.com'
        # Ajoutez ici d'autres données du CV
    }
    return render_template("resume_1.html", cv=cv_data)

# Route pour traiter la mise à jour du CV
@app.route('/update_resume', methods=['POST'])
def update_resume():
    # Récupérer les données soumises depuis le formulaire
    name = request.form['name']
    email = request.form['email']
    # Traiter les autres champs éditables du CV

    # Mettre à jour les données du CV dans la base de données ou un fichier
    # code pour mettre à jour les données du CV
    # ...

    # Rediriger vers la page de visualisation du CV
    return redirect(url_for('resume_1'))

if __name__ == "__main__":
    app.run(debug=True)
