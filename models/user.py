from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Clase base declarativa para los modelos de SQLAlchemy
Base = declarative_base()

# Definir el modelo User
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)  # Columna de clave primaria
    username = Column(String, unique=True, nullable=False)  # Columna de nombre de usuario, única y no nula
    email = Column(String, unique=True, nullable=False)  # Columna de correo electrónico, única y no nula
    role = Column(String, nullable=False)  # Columna de rol, no nula

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', role='{self.role}')>"

# URL de conexión a la base de datos
DATABASE_URL = "sqlite:///./test.db"

# Crear una nueva base de datos SQLite (o conectarse a una existente)
engine = create_engine(DATABASE_URL)

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear una clase de "Sesión" configurada
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para crear un nuevo usuario
def create_user(username: str, email: str, role: str):
    session = SessionLocal()  # Crear una nueva sesión
    try:
        new_user = User(username=username, email=email, role=role)  # Crear un nuevo objeto User
        session.add(new_user)  # Añadir el nuevo usuario a la sesión
        session.commit()  # Confirmar la transacción
        session.refresh(new_user)  # Refrescar la instancia para obtener los nuevos datos de la base de datos
        return new_user  # Devolver el usuario recién creado
    except SQLAlchemyError as e:
        session.rollback()  # Revertir la transacción en caso de error
        print(f"Error creando usuario: {e}")  # Imprimir el mensaje de error
    finally:
        session.close()  # Cerrar la sesión

# Ejemplo de creación de un usuario
if __name__ == "__main__":
    user = create_user("john_doe", "john@example.com", "admin")  # Crear un nuevo usuario
    print(user)  # Imprimir el usuario creado