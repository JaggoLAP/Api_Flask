from ..database import DatabaseConnection

class Servidor:
    
    def __init__(self, **kwargs) -> None:
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre_servidor = kwargs.get('nombre_servidor')
        self.descripcion = kwargs.get('descripcion')
        self.fecha_creacion_servidor = kwargs.get('fecha_creacion_servidor')
        self.imagen_servidor = kwargs.get('imagen_servidor')
        self.id_creador_servidor = kwargs.get('id_creador_servidor')
        self.usuario_id = kwargs.get('usuario_id')
        
    def serialize(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "descripcion": self.descripcion,
            "fecha_creacion_servidor": self.fecha_creacion_servidor,
            "imagen_servidor": self.imagen_servidor,
            "id_creador_servidor": self.id_creador_servidor,
            "usuario_id": self.usuario_id
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
                imagen_servidor=result[4],
                id_creador_servidor=result[5]
            )
        else:
            return None
        
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
                    imagen_servidor=result[4],
                    id_creador_servidor=result[5]
                ))
            return servidores
        else:
            return None
        
    @classmethod
    def get_all_by_user(cls, usuario_id):
        query = '''SELECT s.*, ms.usuario_id FROM devpro.servidores s INNER JOIN devpro.miembro_servidor ms ON s.id_servidor = ms.servidor_id WHERE ms.usuario_id = %s;'''
        params = usuario_id,
        results = DatabaseConnection.fetch_all(query, params=params)
        servidores = []

        if results is not None:
            for result in results:
                servidores.append(cls(
                    id_servidor=result[0],
                    nombre_servidor=result[1],
                    descripcion=result[2],
                    fecha_creacion_servidor=result[3],
                    imagen_servidor=result[4],
                    id_creador_servidor=result[5],
                    usuario_id=result[6]
                ))
            return servidores
        else:
            return None
    
    @classmethod
    def get_by_name(cls, name):
        params = ("%" + name + "%",)
        query = "SELECT * FROM devpro.servidores WHERE nombre_servidor LIKE %s"
        results = DatabaseConnection.fetch_all(query, params=params)
        servidores = []
        if results is not None:
            for result in results:
                servidores.append(cls(
                    id_servidor=result[0],
                    nombre_servidor=result[1],
                    descripcion=result[2],
                    fecha_creacion_servidor=result[3],
                    imagen_servidor=result[4],
                    id_creador_servidor=result[5]
                ))
            return servidores
        else:
            return None

    @classmethod
    def create(cls, servidor):
        query = '''INSERT INTO devpro.servidores (nombre_servidor, descripcion, id_creador_servidor) VALUES (%s, %s, %s)'''
        params = servidor.nombre_servidor, servidor.descripcion, servidor.id_creador_servidor
        cursor = DatabaseConnection.execute_query(query, params=params)
        id_nuevo_servidor = cursor.lastrowid
        query = '''INSERT INTO devpro.miembro_servidor (usuario_id, servidor_id) VALUES (%s, %s)'''
        params = servidor.id_creador_servidor, id_nuevo_servidor
        print(f'query serv model: {query}')
        print(f'params serv model: {params}')
        DatabaseConnection.execute_query(query, params=params)


    @classmethod
    def update(cls, servidor):
        query = '''UPDATE devpro.servidores SET nombre_servidor = %s, descripcion = %s WHERE id_servidor = %s'''
        params = servidor.nombre_servidor, servidor.descripcion, servidor.id_servidor
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, servidor):
        query = '''DELETE FROM devpro.servidores WHERE id_servidor = %s'''
        params = servidor.id_servidor,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def add_serv(cls, servidor):
        query = '''INSERT INTO devpro.miembro_servidor (usuario_id, servidor_id) VALUES (%s, %s)'''
        params = servidor.usuario_id, servidor.servidor_id,
        DatabaseConnection.execute_query(query, params=params)
