from ..database import DatabaseConnection

class Mensaje:
    
    def __init__(self,**kwargs):
        self.id_mensaje=kwargs.get('id_mensaje')
        self.contenido = kwargs.get('contenido')
        self.usuario_id = kwargs.get('usuario_id')
        self.canal_id = kwargs.get('canal_id')
        self.fecha_envio=kwargs.get('fecha_envio')


    def serialize(self):
        return {
            'contenido': self.contenido,
            'usuario_id': self.usuario_id,
            'canal_id': self.canal_id,
            'fecha_envio': self.fecha_envio.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_envio else None
        }

    @classmethod
    def get_mensajes_by_canal(cls,canal_id):
        """Obtener mensajes por canal"""
        query="SELECT * FROM devpro.mensajes WHERE canal_id=%s"
        values=(canal_id,)
        results=DatabaseConnection.fetch_all(query,params=values)
        mensajes_list=[]
        for result in results:
            mensajes_list.append(result)
        return mensajes_list
    
    @classmethod
    def create_mensaje(cls,mensaje):
        query = """INSERT INTO devpro.mensajes(contenido,fecha_envio, usuario_id, canal_id) VALUES(%s,%s,%s,%s)"""
        params=mensaje.contenido, mensaje.fecha_envio,mensaje.usuario_id,mensaje.canal_id,
        DatabaseConnection.execute_query(query,params=params)


    @classmethod
    def delete(cls,id_mensaje,usuario_id):
        query = "SELECT usuario_id FROM devpro.mensajes WHERE id_mensaje=%s"
        values=(id_mensaje,)
        result=DatabaseConnection.execute_query(query,values)

        if result and result[0][0]==usuario_id:
            delete_query="DELETE FROM devpro.mensajes WHERE id_mensaje=%s"
            DatabaseConnection.execute_query(delete_query,values)
        else:
            raise PermissionError("No tienes permiso para eliminar este mensaje")
        
    @classmethod
    def update(cls, mensaje):
        query = "SELECT usuario_id FROM devpro.mensajes WHERE id_mensaje=%s"
        values = mensaje.id_mensaje,
        result = DatabaseConnection.fetch_one(query,params=values)
        
        if result and result[0] == mensaje.usuario_id:
            update_query="UPDATE devpro.mensajes SET contenido = %s WHERE id_mensaje = %s"
            update_values = mensaje.contenido, mensaje.id_mensaje,
            DatabaseConnection.execute_query(update_query, params=update_values)
        else:
            raise PermissionError("No tienes permiso para modificar este mensaje")    





