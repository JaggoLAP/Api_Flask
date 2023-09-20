from ..models.user_model import User

from flask import request, session

class UserController:

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            nombre_usuario = data.get('nombre_usuario'),
            contrasena = data.get('contrasena')
        )
        if User.is_registered(user):
            session['nombre_usuario'] = data.get('nombre_usuario')
            session['servidor_id'] = 1
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401

    @classmethod
    def show_profile(cls):
        nombre_usuario = session.get('nombre_usuario')
        if nombre_usuario is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            print(f'nombre_usuario: {nombre_usuario}')
            print(f'session servidor_id: {session.get("servidor_id")}')
            user = User.get(User(nombre_usuario = nombre_usuario))
            if user is None:
                return {"message": "Usuario no encontrado"}, 404
            else:
                return user.serialize(), 200
    
    @classmethod
    def logout(cls):
        session.pop('nombre_usuario', None)
        session.clear()
        return {"message": "Sesion cerrada"}, 200