from ..models.mensaje_model import Mensaje
from flask import request
from flask import json


class MensajeController:

    @classmethod
    def create_mensaje(cls):
        """Create a new mensaje"""
        data = request.json
        print(f"data: {data}")
        mensaje = Mensaje(**data)
        print(f"mensaje: {mensaje}")
        Mensaje.create_mensaje(mensaje)
        return {'message': 'message created successfully'}, 201

    @classmethod
    def obtener_mensajes_por_canal(cls,canal_id):
        results = Mensaje.get_mensajes_by_canal(canal_id)
        print(f"mensajes: {results}")
        mensajes = []
        for result in results:
            print(f"7 result: {result}")
            mensaje = Mensaje(
                id_mensaje=result[0],
                contenido=result[1],
                fecha_envio=result[2],
                usuario_id=result[3],
                canal_id=result[4]
            )
            print(f"8 canal: {mensaje}")
            mensajes.append(mensaje.serialize())
        
        return mensajes, 200

    @classmethod
    def borrar_mensaje(cls,id_mensaje,usuario_id):
        Mensaje.delete(id_mensaje, usuario_id)
        return {'message': 'Mensaje deleted successfully'}, 204

    
    @classmethod
    def modificar_mensaje(cls,id_mensaje):
        data = request.json
        data['id_mensaje'] = id_mensaje
        print(f"id_mensaje: {data['id_mensaje']}")
        print(f"contenido: {data['contenido']}")
        print(f"usuario_id: {data['usuario_id']}")
        mensaje = Mensaje(**data)
        Mensaje.update(mensaje)
        return {'message': 'Mensaje updated successfully'}, 200
