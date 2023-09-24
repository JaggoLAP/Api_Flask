from ..models.user_models import User
from flask import request

class UserController:
    
    @classmethod
    def get(cls):
        users = []
        for user in User.get():
            users.append(user.serialize())
        return users, 200
    
    @classmethod
    def get_by_id(cls, id_user):
        user=User(user.serialize())
        user=User.get(user)
        if user:
            return user.serialize(), 200
        

    @classmethod
    def create(cls):
        data = request.json
        user = user(**data)
        user.create(user)
        return {'message': 'user created successfully'}, 201
    
    @classmethod
    def update(cls, id_user):
        data = request.json
        data['id_user'] = id_user
        user = user(**data)
        User.update(user)
        return {'message': 'user updated successfully'}, 200
    
    @classmethod
    def delete(cls, id_user):
        user = User(id_user=id_user)
        User.delete(user)
        return {'message': 'User deleted successfully'}, 204
