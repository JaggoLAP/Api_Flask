from ..models.canal_model import Canal
from flask import request, jsonify, session

class CanalController:
    
    @classmethod
    def get(cls, id_canal):
        canal = Canal(id_canal=id_canal)
        result = Canal.get(canal)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_all(cls, servidor_id):
        results = Canal.get_all(servidor_id)
        canales = []
        for result in results:
            canal = Canal(
                id_canal=result[0],
                nombre_canal=result[1],
                servidor_id=result[2],
                fecha_creacion_canal=result[3],
                id_creador_canal=result[4]
            )
            canales.append(canal.serialize())
        return canales, 200

    @classmethod
    def create(cls):
        data = request.json
        canal = Canal(**data)
        Canal.create(canal)
        return {'message': 'Canal created successfully'}, 201

    @classmethod
    def update(cls, id_canal):
        data = request.json
        data['id_canal'] = id_canal
        canal = Canal(**data)
        Canal.update(canal)
        return {'message': 'Canal updated successfully'}, 200

    @classmethod
    def delete(cls, id_canal):
        canal = Canal(id_canal=id_canal)
        Canal.delete(canal)
        return {'message': 'Canal deleted successfully'}, 204

