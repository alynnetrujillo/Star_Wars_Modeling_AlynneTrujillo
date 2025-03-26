from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorites: Mapped[list["Favorite"]] = relationship(back_populates="user")

    def __repr__(self):
        return f'<User {self.email}>'


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            # do not serialize the password, its a security breach
        }
class Character(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    gender: Mapped[str] = mapped_column(String(50))
    height: Mapped[int] = mapped_column(Integer)
    hair_color: Mapped[str] = mapped_column(String(50))
    eye_color: Mapped[str] = mapped_column(String(50))
    birth_year: Mapped[str] = mapped_column(String(50))

    favorites: Mapped[list["Favorite"]] = relationship(back_populates="user")

    def __repr__(self):
        return f'<Character {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
        }
    
class Planet(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    climate: Mapped[str] = mapped_column(String(250))
    gravity: Mapped[str] = mapped_column(String(250))
    terrain: Mapped[str] = mapped_column(String(250))
    population: Mapped[int] = mapped_column(Integer)
    favorites: Mapped[list["Favorite"]] = relationship(back_populates="planet")

    def __repr__(self):
        return f'<Planet {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "population": self.population,
        }

class Favorite(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=True)
    user: Mapped["User"] = relationship(back_populates="favorites")
    character: Mapped["Character"] = relationship(back_populates="favorites")
    planet: Mapped["Planet"] = relationship(back_populates="favorites")

    def __repr__(self):
        return f'<Favorite {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
        }




#User - id, email, password, is_active, favorites
#character - id, name, gender, height, haircolor, eyecolor, birthyear, favs
#planets - id, name, climate, gravity, terrain, population, favorites 
#favorites

