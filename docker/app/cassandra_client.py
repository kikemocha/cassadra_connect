from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

cloud_config = {
    'secure_connect_bundle': 'secure-connect-ksandra.zip'
}

with open("ksandra-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
session.set_keyspace('ksandra')

def get_clientes():
    try:
        rows = session.execute("SELECT * FROM clientes")
        return [row._asdict() for row in rows]
    except Exception as e:
        print("Error al consultar clientes:", e)
        return []

def get_pedidos_por_cliente(cliente_id):
    try:
        rows = session.execute("""
            SELECT * FROM pedidos_por_cliente WHERE cliente_id = %s
        """, (cliente_id,))
        return [row._asdict() for row in rows]
    except Exception as e:
        print("Error al consultar pedidos:", e)
        return []

def get_productos_por_pedido(pedido_id):
    try:
        rows = session.execute("""
            SELECT * FROM productos_por_pedido WHERE pedido_id = %s
        """, (pedido_id,))
        return [row._asdict() for row in rows]
    except Exception as e:
        print("Error al consultar pedidos:", e)
        return []
