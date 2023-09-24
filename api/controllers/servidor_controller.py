from ..models.servidor_model import Servidor
from flask import request, jsonify, session
from ..database import DatabaseConnection

class ServidorController:
    
    @classmethod
    def get(cls, id_servidor):
        servidor = Servidor(id_servidor=id_servidor)
        print(f'1 servidor 1: {servidor}')
        result = Servidor.get(servidor)
        print(f'7 result controller: {result}')
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_all(cls):
        results = Servidor.get_all()
        print(f"6 results: {results}")
        servidores = []
        for result in results:
            print(f"7 result: {result}")
            servidor = Servidor(
                id_servidor=result[0],
                nombre_servidor=result[1],
                descripcion=result[2],
                fecha_creacion_servidor=result[3],
                imagen_servidor=result[4],
                id_creador_servidor=result[5]
            )
            print(f"8 canal: {servidor}")
            servidores.append(servidor.serialize())
        return servidores, 200

    
