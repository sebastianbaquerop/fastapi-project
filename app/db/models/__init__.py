# It is use to import this modules that triggres the class definition to be registered with Base
# the '__init__.py' file acts as a central registry where you explicity import every model file.
# This ensures that when 'main.py' import 'app.db.models', all sub-modules are loaded, registering
# all tables with 'Base' metadata
from app.db.models.base_model import Base
from app.db.models import users, users_and_pokemons 