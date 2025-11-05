"""
Examen Unidad III 
Autor: [Rosales Garcia Oscar]
Fecha: [29/10/2025]

Descripción:
Objetivo del examen
Desarrollar una API básica con Flask que permita:

Crear un diccionario de dispositivos de red.
Agregar nuevos dispositivos.
Modificar dispositivos existentes.
Mostrar un listado de todos los dispositivos en formato HTML, 
donde cada dispositivo se muestre en un <div> con nombre, 
descripción y características

Requisitos técnicos

Usar Flask.
Usar un diccionario como estructura principal de almacenamiento.
Implementar al menos tres rutas:

GET /dispositivos_html: muestra todos los dispositivos en HTML.
POST /dispositivos: agrega un nuevo dispositivo.
PUT /dispositivos/<id>: modifica un dispositivo existente.

Ejemplo del Diccionario de dispositivos: 
{
  "id": "router01",
  "nombre": "Router Principal",
  "descripcion": "Router de borde para salida a Internet",
  "ip": "192.168.1.1",
  "mac": "00:1A:2B:3C:4D:5E",
  "ubicacion": "Sala de servidores",
  "tipo": "Router",
  "otros": ""
}

Recuerda tener al menos 3 commits en tu repositorio. 

Para puntos extra
Puedes ocupar css para añadir puntos a tu examen, perzonalizalo con estilos como el siguiente:
<style>
    .dispositivo {
        border: 1px solid #ccc;
        padding: 10px;
        margin: 10px;
    }
</style>

Puntos extra para añador formula en el cmapo de otros
la formula es la siguente: 

último octeto de la IP * 3 + longitud del nombre del dispositivo + ":" + nombre (Cambiando los espacios por _)

"""
from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

dispositivos = {
}

html = """
<html>
    <body>
        <h1> Lista de dispositivos </h1>

        {% for dispositivo in dispositivos %}
        <div style="border: 1px solid #ccc; margin: 10px">
            <h3> {{ dispositivo.nombre }} </h3>
            <p><strong>"ID:"</strong>{{ dispositivo.id }}</p>
            <p><strong>"Descripcion:"</strong>{{ dispositivo.descripcion }}</p>
            <p><strong>"IP:"</strong>{{ dispositivo.ip }}</p>
            <p><strong>"MAC:"</strong>{{ dispositivo.mac }}</p>
            <p><strong>"Ubicacion:"</strong>{{ dispositivo.ubicacion }}</p>
            <p><strong>"Tipo:"</strong>{{ dispositivo.tipo }}</p>
            <p><strong>"Otros:"</strong>{{ dispositivo.otros }}</p>
        </div>
        {% endfor %}
    </body>
</html>
"""

@app.route('/mostrar', methods=['GET'])
def mostrar_dispositivo():
    dispo_lista = list(dispositivos.values())
    return render_template_string(html, dispositivos = dispo_lista)

@app.route('/agregar', methods=['POST'])
def agregar_dispositivo():
    
    print("Datos recibidos", request.json)
    
    valores = request.json
    
    nuevo_dispo = {
        "id": valores.get('id', ''),
        "nombre": valores.get('nombre', ''),
        "descripcion": valores.get('descripcion', ''),
        "ip": valores.get('ip', ''),
        "mac": valores.get('mac', ''),
        "ubicacion": valores.get('ubicacion', ''),
        "tipo": valores.get('tipo', ''),
        "otros": valores.get('otros', '')
    }

    dispo_id = valores['id']

    dispositivos[dispo_id] = nuevo_dispo 

    return jsonify({
        "mensaje:": "Dispositivo registrado"
    })

@app.route('/modificar/<dispo_id>', methods=['PUT'])
def modificar(dispo_id):
    datos = request.json

    dispo_id = datos['id']

    if dispo_id not in dispositivos:
        html = "<h1>Id no encontrada </h1>"
        return html
    
    dispositivo = dispositivos[dispo_id]

    if 'nombre' in datos:
        dispositivo['nombre']= datos['nombre']
    if 'descripcion' in datos:
        dispositivo['descripcion'] = datos['descripcion']
    if 'ip' in datos:
        dispositivo['ip'] = datos['ip']
    if 'mac' in datos:
        dispositivo['mac'] = datos['mac']
    if 'ubicacion' in datos:
        dispositivo['ubicacion'] = datos['ubicacion']
    if 'tipo' in datos:
        dispositivo['tipo'] = datos['tipo']
    if 'otros' in datos:
        dispositivo['otros'] = datos['otros']

    return jsonify({
        "mensaje": "Dispositivo modificado"
    })
   
   
if __name__ == '__main__':
    app.run(debug=True)