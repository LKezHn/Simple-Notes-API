# Flask RESTX API Demo

API sencilla construida con **Flask**, **MongoDB**, **Flask-RESTX**, **JWT** y **bcrypt**.
Incluye:

* Login, registro y CRUD de tareas (`todos`)
* Autenticación con **JWT**
* Hash de contraseñas con **bcrypt**
* Documentación automática con **Swagger UI**
* Validación de datos en JSON body
* Separación de endpoints públicos y privados

---

## Tecnologías

* Python 3.11+
* Flask
* Flask-RESTX
* Flask-PyMongo
* Flask-JWT-Extended
* bcrypt
* python-dotenv

---

## Estructura del proyecto

```
flask-api-demo/
│
├── app.py                            # Archivo principal
├── config.py                         # Configuración y carga de .env
├── db.py                             # Conexión a MongoDB
├── requirements.txt                  # Dependencias
├── api/                              # Carpeta principal de la API
|   ├── controllers/                  # Carpeta de controllers
|   |   ├── auth_controller.py
|   |   ├── todo_controller.py
|   ├── models/                       # Carpeta de modelos para Swagger
|   |   ├── todo_model.py
|   |   ├── user_model.py
|   ├── namespaces/                   # Carpeta de namespaces
|   |   ├── namespaces.py
|   ├── routes/                       # Carpeta de rutas
|   |   ├── auth_routes.py
|   |   ├── todo_routes.py
```

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/LKezHn/Simple-Notes-API.git
cd Simple-Notes-API
```

2. Crear entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Crear archivo `.env`:

```env
MONGO_URI=mongodb+srv://<usuario>:<password>@cluster.mongodb.net/<dbname>
JWT_SECRET_KEY=tu_clave_secreta
```

---

## Ejecución

```bash
python app.py
```

Swagger UI disponible en:

```
http://localhost:5000/
```

Endpoints principales:

| Endpoint       | Método | Protección |
| -------------- | ------ | ---------- |
| /auth/register | POST   | Público    |
| /auth/login    | POST   | Público    |
| /auth/me       | GET    | JWT        |
| /todo          | GET    | JWT        |
| /todo          | POST   | JWT        |
| /todo/<id>     | GET    | JWT        |
| /todo/<id>     | POST   | JWT        |
| /todo/<id>     | PUT    | JWT        |
| /todo/<id>     | DELETE | JWT        |

---

## Uso de JWT

* Presiona **Authorize** en Swagger UI solo en endpoints privados
* Formato del token:

```
Bearer <tu_token>
```

* El token se envía automáticamente en el header `Authorization`.

---

## Ejemplo de request

**Registro de usuario:**

```http
POST /auth/register
Content-Type: application/json
```

```json
{
  "username": "Juan",
  "email": "juan@email.com",
  "password": "123456"
}
```

**Login:**

```http
POST /auth/login
```

```json
{
  "username": "Juan",
  "password": "123456"
}
```

Respuesta:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Acceso a endpoint protegido:**

```http
GET /users/profile
Authorization: Bearer <token>
```

---

## Buenas prácticas implementadas

* Validación de JSON body con **Flask-RESTX models**
* Hash seguro de contraseñas con **bcrypt**
* Tokens JWT con expiración configurable
* Separación de endpoints públicos y privados para Swagger UI

---

## Notas

* MongoDB requiere que existan **índices únicos** en `username` y `email` para evitar duplicados.
* Para producción, siempre usar **HTTPS**.
* Este proyecto es ideal para **demo de portafolio o prueba técnica**.

---

## Despliegue gratuito recomendado

Puedes desplegar la API fácilmente usando servicios gratuitos:

* **Render:** despliegue gratuito de Flask con MongoDB Atlas.
* **Railway:** rápido y sencillo para proyectos demo.
* **PythonAnywhere:** buena opción para apps pequeñas.

Pasos generales:

1. Subir repositorio a GitHub.
2. Conectar GitHub a Render o Railway.
3. Configurar variables de entorno (`.env`) en la plataforma.
4. Ejecutar `pip install -r requirements.txt` y `python app.py`.

---

## Pruebas con Postman

1. Crear colección `Flask API Demo`.
2. Agregar request `POST /auth/register` con JSON body.
3. Agregar request `POST /auth/login` para obtener token.
4. Guardar token en variable de entorno de Postman.
5. Hacer request a endpoints protegidos usando el header `Authorization: Bearer {{token}}`.

---

## Autor

**Luis Martinez**

---

## Licencia

MIT License
