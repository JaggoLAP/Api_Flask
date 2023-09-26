from ..database import DatabaseConnection

class Canal:
    
    def __init__(self, **kwargs) -> None:
        self.id_canal = kwargs.get('id_canal')
        self.nombre_canal = kwargs.get('nombre_canal')
        self.servidor_id = kwargs.get('servidor_id')
        self.fecha_creacion_canal = kwargs.get('fecha_creacion_canal')
        self.id_creador_canal = kwargs.get('id_creador_canal')

    def serialize(self):
        return {
            "id_canal": self.id_canal,
            "nombre_canal": self.nombre_canal,
            "servidor_id": self.servidor_id,
            "fecha_creacion_canal": self.fecha_creacion_canal,
            "id_creador_canal": self.id_creador_canal
        }
    
    @classmethod
    def get(cls, canal):
        query = '''SELECT * FROM devpro.canales WHERE id_canal = %s'''
        params = canal.id_canal,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_canal = result[0],
                nombre_canal = result[1],
                servidor_id = result[2],
                fecha_creacion_canal = result[3],
                id_creador_canal = result[4]
            )
        else:
            return None
        
    @classmethod
    def get_all(cls, servidor_id):
        query = '''SELECT * FROM devpro.canales WHERE servidor_id = %s'''
        params = servidor_id,
        results = DatabaseConnection.fetch_all(query, params=params)
        canales = []
        if results is not None:
            for result in results:
                canales.append(result)
            return canales
        else:
            return None
        
    @classmethod
    def create(cls, canal):
        query = '''INSERT INTO devpro.canales (nombre_canal, servidor_id, id_creador_canal) VALUES (%s, %s, %s)'''
        params = canal.nombre_canal, canal.servidor_id, canal.id_creador_canal,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, canal):
        query = '''UPDATE devpro.canales SET nombre_canal = %s WHERE id_canal = %s'''
        params = canal.nombre_canal, canal.id_canal,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, canal):
        query = '''DELETE FROM devpro.canales WHERE id_canal = %s'''
        params = canal.id_canal,
        DatabaseConnection.execute_query(query, params=params)