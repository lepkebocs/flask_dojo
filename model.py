from peewee import *



# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase("flask_dojo", 'kadartamas')


class BaseModel(Model):  # Main Class with the database connection.
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db

class Counter(BaseModel):
    counter = IntegerField(default=0)

db.connect()
db.create_tables([Counter], safe=True)
