from flask import Flask, render_template, request, redirect, url_for
from static.build.model import * # type: ignore

app = Flask(__name__)

# ROTA INICIAL, RETORNA TODOS OS DADOS NA TEBELA
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        name = request.form['name_product'] # ATRIBUINDO O VALOR DO INPUT, PARA A VARIÉVEL name
        add_item(name) # ADICIONANDO NOVO  ELEMENTO AO BANCO DE DADOS
    return render_template("index.html", dados=show_All())


# ROTA PARA ALTERAÇÃO DE ELEMENTOS
@app.route("/alter/<string:id>", methods=["GET", "POST"])
def alter(id):
    if request.method == 'POST':
        name = request.form['name_product']
        alter_item(name, int(id))
        return redirect(url_for('index'))
    return render_template('update.html')

# ROTA PARA EXCLUSÃO DE ELEMENTOS 
@app.route("/delete/<string:id>", methods=["GET", "POST"])
def delete(id):
    delete_item(id)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)