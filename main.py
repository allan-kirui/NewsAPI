from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, aliased
from database import crud, database
from database.models import Location, Person, News, NewsAssociation


if __name__ == '__main__':
    session = database.session

    # Create aliases for the joined tables
    news_alias = aliased(News, name='news_alias')
    locations_alias = aliased(Location, name='locations_alias')
    people_alias = aliased(Person, name='people_alias')
    news_association_alias = aliased(NewsAssociation, name='news_association')

    query = (
        session.query(
            news_alias.id.label('news_id'),
            news_alias.title,
            news_alias.content,
            news_alias.date,
            locations_alias.name.label('location_name'),
            people_alias.name.label('person_name'),
            people_alias.surname
        )
        .join(news_association_alias, news_alias.id == news_association_alias.news_id)
        .join(locations_alias, news_association_alias.location_id == locations_alias.id)
        .join(people_alias, news_association_alias.person_id == people_alias.id)
    )
    # Execute the query and fetch the results
    results = query.all()

    # Display the results
    for result in results:
        print(result)
