from ..database import DatabaseConnection
from datetime import datetime

class Mensaje:
    
    def __init__(self,**kwargs):
        self.id_mensaje=kwargs.get('id_mensaje')
        self.contenido = kwargs.get('contenido')
        self.usuario_id = kwargs.get('usuario_id')
        self.canal_id = kwargs.get('canal_id')
        self.fecha_envio=kwargs.get('fecha_envio')
        self.nombre_usuario=kwargs.get('nombre_usuario')


    def serialize(self):
        return {
            'id_mensaje': self.id_mensaje,
            'contenido': self.contenido,
            'usuario_id': self.usuario_id,
            'canal_id': self.canal_id,
            'fecha_envio': self.fecha_envio.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_envio else None,
            'nombre_usuario': self.nombre_usuario
        }

    @classmethod
    def get_mensajes_by_canal(cls,canal_id):
        #query="SELECT * FROM devpro.mensajes WHERE canal_id=%s"
        query='''SELECT m.*, u.nombre_usuario
FROM devpro.mensajes m
INNER JOIN devpro.usuarios u ON m.usuario_id = u.id_usuario
WHERE m.canal_id = %s ORDER BY id_mensaje ASC LIMIT 30;'''
        print(f'query model: {query}')
        values=(canal_id,)
        print(f'values model: {values}')
        results=DatabaseConnection.fetch_all(query,params=values)
        mensajes_list=[]
        for result in results:
            mensajes_list.append(result)
        return mensajes_list
    
    @classmethod
    def create_mensaje(cls,mensaje):
        now = datetime.now()
        fecha_hora_actual = now.strftime("%Y-%m-%d %H:%M:%S")
        query = """INSERT INTO devpro.mensajes(contenido,fecha_envio, usuario_id, canal_id) VALUES(%s,%s,%s,%s)"""
        params = mensaje.contenido, fecha_hora_actual, mensaje.usuario_id, mensaje.canal_id,
        DatabaseConnection.execute_query(query,params=params)


    @classmethod
    def delete(cls,id_mensaje,usuario_id):
        query = '''SELECT usuario_id FROM devpro.mensajes WHERE id_mensaje=%s;'''
        print(f'query model: {query}')
        params = id_mensaje,
        print(f'params model: {params}')
        result = DatabaseConnection.execute_query(query, params=params)
        
        print(f'result-0 model: {result.fetchone()[0]}')
        if result.fetchone()[0] == usuario_id:
            delete_query = '''DELETE FROM devpro.mensajes WHERE id_mensaje=%s;'''
            DatabaseConnection.execute_query(query, params=params)
            print(f'echo model: {delete_query}')
        else:
            raise PermissionError("No tienes permiso para eliminar este mensaje")
        
    @classmethod
    def update(cls, mensaje, usuario_id):
        query = "SELECT usuario_id FROM devpro.mensajes WHERE id_mensaje=%s"
        values = mensaje.id_mensaje,
        result = DatabaseConnection.fetch_one(query,params=values)
        
        if result and result[0] == usuario_id:
            update_query="UPDATE devpro.mensajes SET contenido = %s WHERE id_mensaje = %s"
            update_values = mensaje.contenido, mensaje.id_mensaje,
            DatabaseConnection.execute_query(update_query, params=update_values)
        else:
            raise PermissionError("No tienes permiso para modificar este mensaje")    





