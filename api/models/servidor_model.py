from ..database import DatabaseConnection

class Servidor:
    
    def __init__(self, **kwargs) -> None:
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre_servidor = kwargs.get('nombre_servidor')
        self.descripcion = kwargs.get('descripcion')
        self.fecha_creacion_servidor = kwargs.get('fecha_creacion_servidor')
        self.imagen_servidor = kwargs.get('imagen_servidor')
        self.id_creador_servidor = kwargs.get('id_creador_servidor')
        
    def serialize(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "descripcion": self.descripcion,
            "fecha_creacion_servidor": self.fecha_creacion_servidor,
            "imagen_servidor": self.imagen_servidor,
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
                imagen_servidor=result[4],
                id_creador_servidor=result[5]
            )
        else:
            return None
        
    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM devpro.servidores'''
        #params = servidor_id,
        print(f"2 query: {query}")
        #print(f"3 params: {params}")
        results = DatabaseConnection.fetch_all(query)
        print(f"5 results: {results}")
        servidores = []
        if results is not None:
            for result in results:
                servidores.append(result)
            return servidores
        else:
            return None
        
    @classmethod
    def create(cls, canal):
        query = '''INSERT INTO devpro.canales /
                (nombre_canal, servidor_id, id_creador_canal) /
                VALUES (%s, %s, %s)'''

        params = canal.nombre_canal, canal.servidor_id, canal.id_creador_canal
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, canal):
        query = '''UPDATE devpro.canales SET nombre_canal = %s WHERE id_canal = %s'''

        params = canal.nombre_canal, canal.id_canal
        DatabaseConnection.execute_query(query, params=params)
