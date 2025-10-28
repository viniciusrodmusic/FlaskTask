from flask import Flask, flash, render_template, redirect, url_for, request
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

DB_NAME = "todo_flask"

criar_tabela = (
    """
    CREATE TABLE IF NOT EXISTS tarefas(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nome_tarefa VARCHAR(100) NOT NULL,
        data_criacao DATETIME NOT NULL
    );
    """
)


# Conectando-se ao banco MySQL
try:
    conexao = mysql.connector.connect(
        user="root",
        host="localhost",
        password="",
        database="todo_flask"
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Algo está errado com seu usuário ou senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe")


cursor = conexao.cursor()
cursor.execute(criar_tabela)
cursor.close()





# Aplicação
app = Flask(__name__)
app.secret_key = "chave-padrao"


@app.route("/", methods=["GET", "POST"])
def home():
    contagem = 0 # Registros na tabela
    # Criando cursor
    cursor = conexao.cursor()
    # Trazendo dados da tabela
    try:
        cursor.execute("SELECT * FROM tarefas;")
        resposta = cursor.fetchall()

        cursor.execute("SELECT COUNT(*) FROM tarefas;")
        contagem = cursor.fetchone()[0]

    except mysql.connector.Error as err:
        print(err)

    
    if request.method == "POST":
        if contagem == 5:
            flash("Você chegou ao limite de 5 tarefas", "info")
            return redirect(url_for("home"))

        nome_tarefa = request.form.get("nome_tarefa")
        data_criacao = datetime.now()
      
        # executar o INSERT INTO aqui
        cursor.execute("INSERT INTO tarefas(nome_tarefa, data_criacao) VALUES (%s, %s)", (nome_tarefa, data_criacao))
        # dá commit
        conexao.commit()
        cursor.close()
    
        # Depois redirecionar pra mesma rota
        return redirect(url_for("home"))
   

    return render_template("home.html", tarefas=resposta)


9



@app.route("/delete/<int:id>")
def delete(id):

    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM tarefas WHERE id = %s;", (id,))
        conexao.commit()
    except mysql.connector.Error as err:
        print(err.errno)
    cursor.close()

    return redirect(url_for("home"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cursor = conexao.cursor()

    if request.method == "POST":
        novo_nome = request.form.get("tarefa_nova")
        try:
            cursor.execute("UPDATE tarefas SET nome_tarefa = %s WHERE id = %s;", (novo_nome, id))
            conexao.commit()
            flash("Tarefa alterada com sucesso!", "success")
            return redirect(url_for("home"))
        
        except mysql.connector.Error as err:
            print(err.errno)
            return redirect(url_for("home"))
        
    cursor.close()

    return render_template("edit.html", id=id)





if __name__ == '__main__':
    app.run(debug=True)