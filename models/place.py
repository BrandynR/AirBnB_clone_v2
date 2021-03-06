#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy import Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.city import City
from models.user import User
from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", "place")

    amenities = relationship(
        "Amenity",
        secondary="place_amenity",
        viewonly=False, backref="place")

    @property
    def reviews(self):
        """ getter attribute for reviews of places """
        obj = storage.all()
        reviews = []
        print("OBJ:", obj)
        print("MY DICT:", my_dict)
        for key, value in my_dict.items():
            if "Review" in key and value.place_id == self.id:
                reviews.append(value)
        return reviews

    @property
    def amenities(self):
        """ getter attribute for amenities of places """
        obj = storage.all()
        amenities = []
        for key, value in obj:
            if "Amenity" in key and value.place_id == self.id:
                amenities.append(value)
        return amenities
