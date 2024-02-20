
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Vous pouvez charger main.yml ici pour afficher les liens
    links = load_links_from_yaml("main.yml")
    return render_template("index.html", links=links)

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

def load_links_from_yaml(yaml_file):
    # Fonction pour charger les liens depuis un fichier YAML
    # Ici, vous pouvez utiliser une bibliothèque comme PyYAML pour charger le fichier YAML
    # et extraire les liens
    # Dans cet exemple, nous simulons simplement le chargement de liens statiques
    with open(yaml_file, 'r') as file:
        links_data = yaml.load(file, Loader=yaml.FullLoader)
    return links_data['links']

if __name__ == "__main__":
    app.run()
