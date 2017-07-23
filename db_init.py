# (re)Initialize database with categories.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import *

"""Used for seeding the database for testing and dev purposes"""
engine = create_engine('sqlite:///catalog.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Clear the tables
session.query(Category).delete()
session.query(Item).delete()

# Add categories
session.add_all([
    Category(name="Soccer"),
    Category(name="Basketball"),
    Category(name="Baseball"),
    Category(name="Snowboarding"),
    Category(name="Football"),
    Category(name="Hockey")])
session.commit()

print "Database has been reset and categories were added :)"
print "You can add items in categories once you are logged in."
