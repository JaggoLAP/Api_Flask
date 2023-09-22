from ..database import DatabaseConnection

class Servidor:
    
    def __init__(self, **kwargs) -> None:
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre_servidor = kwargs.get('nombre_servidor')
        self.descripcion = kwargs.get('descripcion')
        self.fecha_creacion_servidor = kwargs.get('fecha_creacion_servidor')
        self.id_creador_servidor = kwargs.get('id_creador_servidor')

    def serialize(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "descripcion": self.descripcion,
            "fecha_creacion_servidor": self.fecha_creacion_servidor,
            "id_creador_servidor": self.id_creador_servidor
        }
    
    @classmethod
    def get(cls, servidor):
        query = '''SELECT * FROM devpro.servidores WHERE id_servidor = %s'''
        params = servidor.id_servidor,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_servidor=result[0],
                nombre_servidor=result[1],
                descripcion=result[2],
                fecha_creacion_servidor=result[3],
                id_creador_servidor=result[4]
            )
        else:
            return None
    """  
    @classmethod
    def get_all(cls, id_creador_servidor):
        query = '''SELECT * FROM devpro.servidores WHERE id_creador_servidor = %s'''
        params = id_creador_servidor,
        results = DatabaseConnection.fetch_all(query, params=params)
        servidores = []

        if results is not None:
            for result in results:
                servidores.append(result)
            return servidores
        else:
            return None"""
    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM devpro.servidores'''
        results = DatabaseConnection.fetch_all(query)
        servidores = []

        if results is not None:
            for result in results:
                servidores.append(cls(
                    id_servidor=result[0],
                    nombre_servidor=result[1],
                    descripcion=result[2],
                    fecha_creacion_servidor=result[3],
                    id_creador_servidor=result[4]
                ))
            return servidores
        else:
            return None
        
    @classmethod
    def create(cls, servidor):
        query = '''INSERT INTO devpro.servidores (nombre_servidor, descripcion, id_creador_servidor) VALUES (%s, %s, %s)'''

        params = servidor.nombre_servidor, servidor.descripcion, servidor.id_creador_servidor
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, servidor):
        query = '''UPDATE devpro.servidores SET nombre_servidor = %s, descripcion = %s WHERE id_servidor = %s'''

        params = servidor.nombre_servidor, servidor.descripcion, servidor.id_servidor
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, id_servidor):
        query = '''DELETE FROM devpro.servidores WHERE id_servidor = %s'''
        params = id_servidor
        DatabaseConnection.execute_query(query, params=params)



