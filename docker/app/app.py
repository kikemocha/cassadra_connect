from flask import Flask, render_template
from cassandra_client import get_clientes, get_pedidos_por_cliente, get_productos_por_pedido

app = Flask(__name__)

@app.route("/")
def home():
    clientes = get_clientes()
    return render_template("home.html", clientes=clientes)

@app.route("/cliente/<uuid:cliente_id>")
def detalle_cliente(cliente_id):
    pedidos = get_pedidos_por_cliente(cliente_id)
    return render_template("detalle_clientes.html", pedidos=pedidos, cliente_id=cliente_id)

@app.route('/pedido/<uuid:pedido_id>')
def detalle_pedido(pedido_id):
    productos = get_productos_por_pedido(pedido_id)
    return render_template("detalle_pedidos.html", productos=productos, pedido_id=pedido_id)

if __name__ == "__main__":
    app.run(debug=True)


