from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Création de l'application Flask

@app.route('/')
def home():
    return render_template("resume_1.html")

@app.route('/update_resume', methods=['POST'])
def update_resume():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']
        # Récupérer d'autres champs de formulaire de la même manière
        
        # Mettre à jour les données dans votre application (par exemple, dans une base de données)
        # Ici, nous ne faisons que renvoyer les données pour l'exemple
        updated_data = {
            'name': name,
            'dob': dob,
            'email': email,
            # Ajouter d'autres champs mis à jour de la même manière
        }
        
        # Rediriger vers la page d'accueil avec un message de confirmation ou afficher un message sur la page
        return render_template("resume_1.html", updated_data=updated_data)

if __name__ == "__main__":
    app.run()

