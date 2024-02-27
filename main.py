from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from locations.locations_api import router as location_router
from people.people_api import router as people_router

description = """
NewsAPI helps you get the latest news. 🚀
"""

app = FastAPI(
    title="NewsAPI",
    description=description,
    summary="The future is here.",
    contact={
        "name": "Allan Kirui",
        "url": "https://www.linkedin.com/in/allan-kirui-bb55921b4/",
        "email": "https://github.com/allan-kirui/",
    },
    license_info={
        "name": "Creative Commons Attribution-NonCommercial 4.0 International License",
        "url": "https://creativecommons.org/licenses/by-nc/4.0/",
    }
)


# Redirect from "/" to "/newsApi"
@app.get("/")
async def read_root():
    return RedirectResponse(url="/newsApi", status_code=301)


# Include routers
app.include_router(location_router, prefix="/newsApi/locations", tags=["locations"])
app.include_router(people_router, prefix="/newsApi/people", tags=["people"])

# # Create aliases for the joined tables
# news_alias = aliased(News, name='news_alias')
# locations_alias = aliased(Location, name='locations_alias')
# people_alias = aliased(Person, name='people_alias')
# news_association_alias = aliased(NewsAssociation, name='news_association')
#
# query = (
#     session.query(
#         news_alias.id.label('news_id'),
#         news_alias.title,
#         news_alias.content,
#         news_alias.date,
#         locations_alias.name.label('location_name'),
#         people_alias.name.label('person_name'),
#         people_alias.surname
#     )
#     .join(news_association_alias, news_alias.id == news_association_alias.news_id)
#     .join(locations_alias, news_association_alias.location_id == locations_alias.id)
#     .join(people_alias, news_association_alias.person_id == people_alias.id)
# )
# # Execute the query and fetch the results
# results = query.all()
#
# # Display the results
# for result in results:
#     print(result)
