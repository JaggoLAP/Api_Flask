from ..models.servidor_model import Servidor
from flask import request, jsonify

class ServidorController:

    @classmethod
    def get(cls, id_servidor):
        servidor = Servidor(id_servidor=id_servidor)
        result = Servidor.get(servidor)
        if result is not None:
            return result.serialize(), 200
        else:
            return {"message": "Servidor no encontrado"}, 404

    @classmethod
    def get_all(cls):
        results = Servidor.get_all()
        if results is not None:
            servidores = [servidor.serialize() for servidor in results]
            return servidores, 200
        else:
            return {"message": "No se encontraron servidores"}, 404

    @classmethod
    def create(cls):
        data = request.json
        nuevo_servidor = Servidor(**data)
        Servidor.create(nuevo_servidor)
        return {"message": "Servidor creado exitosamente"}, 201

    @classmethod
    def update(cls, id_servidor):
        data = request.json
        data['id_servidor'] = id_servidor
        servidor_actualizado = Servidor(**data)
        Servidor.update(servidor_actualizado)
        return {"message": "Servidor actualizado exitosamente"}, 200

    @classmethod
    def delete(cls, id_servidor):
        servidor = Servidor(id_servidor=id_servidor)
        Servidor.delete(servidor)
        return {"message": "Servidor eliminado exitosamente"}, 204
