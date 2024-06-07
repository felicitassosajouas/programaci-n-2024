from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pizzeria'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/pedidos", methods=["POST"])
def pedidos():
    if request.method == "POST":
        
        id_cliente = request.form["id_cliente"]
        fullname = request.form["nombre"]
        direccion = request.form["direccion"]
        phone = request.form["tel"]
        tipo_pizza = request.form["tipo_pizza"]
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO pedido (id_cliente, nombre, direccion, tel, tipo_pizza) VALUES (%s,%s,%s,%s,%s)',(id_cliente, fullname, direccion, phone, tipo_pizza))
        mysql.connection.commit()
        return render_template("pedido.html")
    

@app.route("/menu")
def menu():
    return render_template("menu.html")



if __name__=="__main__":
    app.run(port=5021,debug=True)