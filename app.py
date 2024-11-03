from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def insert_into_database(name, email, phone, message):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='@LupaMavibe#2004',
            database='dbservicos'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_query = """ INSERT INTO contato (nome, email, telefone, mensagem)
                                   VALUES (%s, %s, %s, %s)"""
            record_tuple = (name, email, phone, message)
            cursor.execute(sql_insert_query, record_tuple)
            connection.commit()
            cursor.close()
            connection.close()
        return True
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return False

@app.route('/')
def contact_form():
    return render_template('contato.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    if insert_into_database(name, email, phone, message):
        return redirect(url_for('confirmation'))
    else:
        return "Erro ao inserir os dados no banco de dados."

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == "__main__":
    app.run(debug=True)
