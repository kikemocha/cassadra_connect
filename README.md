# Flask + Cassandra (AstraDB) App

Esta es una aplicación web sencilla desarrollada con **Flask** que se conecta a una base de datos **Cassandra** (usando **Astra DB**) para mostrar información de clientes, pedidos y productos. Todo está montado con **Docker** para facilitar el despliegue y desarrollo.

---

## 🧱 Estructura

La app permite:

- Mostrar una lista de clientes
- Ver los pedidos de un cliente
- Ver los productos de un pedido

---

## ✨ Requisitos

1. Tener una cuenta gratuita en [Astra DB](https://www.datastax.com/astra)
2. Crear una base de datos **nueva** con el nombre **`ksandra`**
3. Descargar desde Astra:
   - `secure-connect-ksandra.zip`
   - `ksandra-token.json`
4. Colocar los archivos en estas rutas del proyecto:

```
# .gitignore (estos archivos están ignorados)
ksandra-token.json  
secure-connect-ksandra.zip

docker/ksandra-token.json
docker/secure-connect-ksandra.zip
```

---

## 📄 Tablas necesarias en la base de datos `ksandra`

| Tabla                  | Descripción                                | Clave primaria                 |
|------------------------|--------------------------------------------|-------------------------------|
| `clientes`             | Información de los clientes                | `cliente_id`                  |
| `pedidos_por_cliente` | Pedidos hechos por un cliente              | `(cliente_id, pedido_id)`     |
| `pedidos_por_fecha`   | Pedidos ordenados por fecha                | `(fecha, pedido_id)`          |
| `productos_por_pedido`| Productos asociados a un pedido            | `(pedido_id, producto_id)`    |

> Asegúrate de usar exactamente este esquema para que la app funcione correctamente.

---

## 🚧 Uso con Docker

### 1. Construye el contenedor

```bash
docker compose build
```

### 2. Inicia la aplicación

```bash
docker compose up
```

La app se ejecutará en:  
📍 [http://localhost:5000](http://localhost:5000)

---

## 📁 Estructura del proyecto

```
.
├── app
│   ├── app.py                  # Aplicación principal Flask
│   ├── cassandra_client.py     # Conexión y funciones con Cassandra
│   ├── ksandra-token.json      # (No versionado) Token de Astra
│   ├── secure-connect-ksandra.zip  # (No versionado) Bundle de conexión segura
│   └── templates/
│       ├── home.html
│       ├── detalle_cliente.html
│       └── detalle_pedidos.html
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⛔️ Notas

- Esta app es solo para **desarrollo**. No uses este servidor Flask en producción.
- Flask está en modo `development` para que detecte automáticamente los cambios al guardar.
- Los archivos `.zip` y `.json` **no deben subirse al repositorio** (están en `.gitignore`).

---

## ✉️ Autor

Desarrollado por Kike ⚡

