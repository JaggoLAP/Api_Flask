from ..models.servidor_model import Servidor
from flask import request, session


class ServidorController:
    
    @classmethod
    def get(cls, id_servidor):
        nombre_usuario = session.get('nombre_usuario')
        if nombre_usuario is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            servidor = Servidor(id_servidor=id_servidor)
            result = Servidor.get(servidor)
            if result is not None:
                return result.serialize(), 200

    @classmethod
    def get_all(cls):
        nombre_usuario = session.get('nombre_usuario')
        if nombre_usuario is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            results = Servidor.get_all()
            servidores = []
            for result in results:
                servidores.append(result.serialize())
            return servidores, 200
        
    @classmethod
    def get_all_by_user(cls):
        nombre_usuario = session.get('nombre_usuario')
        if nombre_usuario is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            usuario_id = session.get('id_usuario')
            print(f'nombre_usuario: {nombre_usuario}')
            print(f'usuario_id: {usuario_id}')
            results = Servidor.get_all_by_user(usuario_id)
            servidores = []
            for result in results:
                servidores.append(result.serialize())
            return servidores, 200
    
    @classmethod
    def get_by_name(cls, string_param):
        nombre_usuario = session.get('nombre_usuario')
        if nombre_usuario is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            results = Servidor.get_by_name(string_param)
            servidores = []
            for result in results:
                servidores.append(result.serialize())
            return servidores, 200

    @classmethod
    def create(cls):
        nombre_usuario = session.get('nombre_usuario')
        if nombre_usuario is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
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
        print(f'servidor: {servidor}')
        Servidor.delete(servidor)
        return {"message": "Servidor eliminado exitosamente"}, 204

    @classmethod
    def add_serv(cls, id_servidor):
        data = request.json
        agregar_serv_user = Servidor(**data)
        Servidor.add_serv(agregar_serv_user)
        return {"message": "Usuario agregado al servidor exitosamente"}, 201