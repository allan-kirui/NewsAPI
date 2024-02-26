from sqlalchemy.orm import Session
from database.models import Location

def create_location(db: Session, name: str):
    location = Location()
    db.add(location)
    db.commit()
    db.refresh(location)
    return location
#
# def create_person(db: Session, name: str):
#     person = Person()
#     db.add(person)
#     db.commit()
#     db.refresh(person)
#     return person
#
# def create_news(db: Session, title: str, content: str, location_id: int, person_id: int):
#     news = News()
#     db.add(news)
#     db.commit()
#     db.refresh(news)
#     return news
#
# def get_news_by_entity(db: Session, entity_type: str, entity_id: int):
#     if entity_type.lower() == "location":
#         entity = db.query(Location).filter(Location.id == entity_id).first()
#     elif entity_type.lower() == "person":
#         entity = db.query(Person).filter(Person.id == entity_id).first()
#     else:
#         return None
#
#     if not entity:
#         return None
#
#     return db.query(News).filter(
#         ((News.location_id == entity_id) & (entity_type.lower() == "location")) |
#         ((News.person_id == entity_id) & (entity_type.lower() == "person"))
#     ).all()
