from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = "athena_space_secret"  # necessário para flash

# -----------------------------
# CARREGAR DADOS
# -----------------------------
def load_projects():
    with open("data/projects.json", encoding="utf-8") as f:
        return json.load(f)

# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def home():
    projects = load_projects()
    query = request.args.get("q", "").lower()

    if query:
        projects = [
            p for p in projects
            if query in p["nome"].lower()
        ]

    return render_template("index.html", projects=projects)

# -----------------------------
# DETALHE DO PROJETO
# -----------------------------
@app.route("/project/<int:project_id>")
def project_detail(project_id):
    projects = load_projects()

    project = next(
        (p for p in projects if p["id"] == project_id),
        None
    )

    if not project:
        flash("Projeto não encontrado!")
        return redirect(url_for("home"))

    return render_template("project.html", project=project)

# -----------------------------
# API JSON
# -----------------------------
@app.route("/api/projects")
def projects_api():
    return jsonify(load_projects())

# -----------------------------
# EXEMPLO DE AÇÃO (FLASH)
# -----------------------------
@app.route("/add-task", methods=["POST"])
def add_task():
    flash("Tarefa adicionada com sucesso!")
    return redirect(url_for("home"))

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)