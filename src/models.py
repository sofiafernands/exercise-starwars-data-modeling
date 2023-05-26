import os, sys#bibliotecas estandar de Python utilizadas para funcionalidades del sistema operativo y ejecucion del programa.
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base() #esta  funcion proporcionada por sqlalqhemy (declarative_base)sera la base para definir los modelos de las tablas.

# Se definen varias clases(tablas) que representan las tablas en la base de datos. Cada clase hereda de la clase Base definida anteriormente.
class User(Base):
        __tablename__ = 'user'  #__tablename__ Especifica el nombre de la tabla en la base de datos para cada clase.
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        email = Column(String(250), nullable=False)
        favorites_planets = relationship('FavoritesPlanets', backref='user', lazy=True) #Se definen relaciones entre las tablas utilizando la función relationship de SQLAlchemy.
        favorites_characters = relationship('FavoritesCharacters', backref='user', lazy=True) #Se definen relaciones entre las tablas utilizando la función relationship de SQLAlchemy.
        favorites_vehicles = relationship('FavoritesVehicles', backref='user', lazy=True) #Se definen relaciones entre las tablas utilizando la función relationship de SQLAlchemy.

class Characters(Base):
        __tablename__ = 'characters'
        # Aquí definimos columnas para la dirección de la tabla.
        # Tenga en cuenta que cada columna también es un atributo de instancia de Python normal.
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        gender = Column(String(250), nullable=False)
        eye_color = Column(String(250), nullable=False)
             #backref='characters' crea un atributo en la tabla characters que permite acceder a los registros relacionados en la tabla FavoritesCharacters, y 
            # lazy=True configura la carga diferida de los registros relacionados, cargandolos solo cuando se accede a ellos explicitamente.
        favorites_character = relationship('FavoritesCharacters', backref='characters', lazy=True) #backref en SQLAlchemy es utilizada para establecer una relacion
                                                                                                #bidireccional entre las tablas. En este caso, cuando se establece 
                                                                                                # backref='characters' en la relación de la tabla FavoritesCharacters, se crea 
                                                                                                # automáticamente un atributo adicional en la tabla Characters que permite 
                                                                                                # acceder a los registros relacionados en la tabla FavoritesCharacters

class Planets(Base):
        __tablename__ = 'planets'
        # Aquí definimos columnas para la dirección de la tabla.
        # Tenga en cuenta que cada columna también es un atributo de instancia de Python normal.
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False) 
        terrain = Column(String(250), nullable=False)
        population = Column(String(250), nullable=False)
        favorites_planets = relationship('FavoritesPlanets', backref='planets', lazy=True) #lazy=True se utiliza para configurar la carga diferida (lazy loading) de los 
                                                                                           #registros relacionados. Con lazy=True, los registros relacionados se cargarán 
                                                                                           # solo cuando se acceda a ellos explícitamente. Esto puede ser util para mejorar el
                                                                                           #  rendimiento, ya que evita la carga de todos los registros relacionados de forma 
                                                                                           # automatica.
class Vehicles(Base):
        __tablename__ = 'vehicles'
        # Here we define columns for the table person
        # Notice that each column is also a normal Python instance attribute.
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        passengers = Column(String(250), nullable=False)
        type = Column(String(250), nullable=False)
        favorites_vehicles = relationship('FavoritesVehicles', backref='vehicles', lazy=True) #

class FavoritesCharacters(Base):
        __tablename__ = "favoritescharacters"
        id = Column (Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)

class FavoritesPlanets(Base):
        __tablename__ = "favoritesplanets"
        id = Column (Integer, primary_key=True)
        planet_id = Column(Integer, ForeignKey('planets.id'))
        user_id = Column(Integer, ForeignKey('user.id'), nullable=False)



class FavoritesVehicles(Base):
        __tablename__ = "favoritesvehicles"
        id = Column (Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)

   
        
        # def to_dict(self): #esta función se implementaría para convertir un objeto de la clase en un diccionario, en este caso no es necesario ya que no lo estamos
                             #retornando en formato diccionario
        #         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png') #La función render_er se llama con los argumentos Base y 'diagram.png'.
                                #Genera un diagrama ER(entidad relaciones) en formato PNG a partir de los 
                                # modelos definidos en SQLAlchemy y lo guarda como "diagram.png" en el directorio actual, para obtenerlo graficamente, escribimos en 
                                #la terminal $ pipenv run diagram
