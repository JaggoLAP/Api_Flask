from ..models.canal_model import Canal
from flask import request, jsonify, session

class CanalController:
    
    @classmethod
    def get(cls, id_canal):
        canal = Canal(id_canal=id_canal)
        print(f'1 canal 1: {canal}')
        result = Canal.get(canal)
        print(f'7 result controller: {result}')
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def get_all(cls, servidor_id):
        print(f'1 servidor_id: {servidor_id}')
        results = Canal.get_all(servidor_id)
        print(f"6 results: {results}")
        canales = []
        for result in results:
            print(f"7 result: {result}")
            canal = Canal(
                id_canal=result[0],
                nombre_canal=result[1],
                servidor_id=result[2],
                fecha_creacion_canal=result[3],
                id_creador_canal=result[4]
            )
            print(f"8 canal: {canal}")
            canales.append(canal.serialize())
        return canales, 200

    @classmethod
    def create(cls):
        data = request.json
        canal = Canal(**data)
        Canal.create(canal)
        print(f'params controller resultado: {canal}')
        return {'message': 'Canal created successfully'}, 201

    @classmethod
    def update(cls, id_canal):
        data = request.json
        data['id_canal'] = id_canal
        canal = Canal(**data)
        print(f'id_canal controller: {data["id_canal"]}')
        print(f'nombre_canal controller: {data["nombre_canal"]}')
        Canal.update(canal)
        return {'message': 'Canal updated successfully'}, 200

    @classmethod
    def delete(cls, id_canal):
        canal = Canal(id_canal=id_canal)
        Canal.delete(canal)
        return {'message': 'Canal deleted successfully'}, 204



