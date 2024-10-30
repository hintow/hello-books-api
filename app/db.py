from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models.base import Base
'''
create an instance of SQLAlchemy, which we will call db, 
and pass it our Base class as the constructor argument. 
We will use the db object when we need to interact with 
the database to perform operations like creating 
or updating records.
'''
db = SQLAlchemy(model_class=Base)
migrate = Migrate()