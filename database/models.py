import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Table, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.base import Base


# Association Table
class NewsAssociation(Base):
    __tablename__ = 'news_association'
    news_id = Column(UUID(as_uuid=True), ForeignKey('news.id'), primary_key=True)
    location_id = Column(UUID(as_uuid=True), ForeignKey('locations.id'), primary_key=True)
    person_id = Column(UUID(as_uuid=True), ForeignKey('people.id'), primary_key=True)


class Location(Base):
    __tablename__ = 'locations'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    # Define the relationship with News using the association table
    news = relationship('News', secondary=NewsAssociation.__tablename__, back_populates='locations', overlaps="news")


class Person(Base):
    __tablename__ = 'people'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    # Define the relationship with News using the association table
    news = relationship('News', secondary=NewsAssociation.__tablename__, back_populates='people', overlaps="news")


class News(Base):
    __tablename__ = 'news'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, index=True)
    content = Column(String)
    date = Column(DateTime)
    # Define the relationship with Location and Person
    locations = relationship('Location', secondary=NewsAssociation.__tablename__, back_populates='news', viewonly=True)
    people = relationship('Person', secondary=NewsAssociation.__tablename__, back_populates='news', viewonly=True)
