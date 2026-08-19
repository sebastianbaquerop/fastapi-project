import inspect 
#  ----- Audit Alembic
# import datetime

from logging.config import fileConfig

from sqlalchemy import create_engine, engine_from_config, text
from sqlalchemy import pool

from alembic import context

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

#  ----- Audit Alembic
# import audit_alembic

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from app.db.models.base_model import Base
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

#  ----- Audit Alembic
# Define your application's current software semantic version
#APP_VERSION = "1.0.0" 

#  ----- Audit Alembic
# 3. INITIALIZE THE AUTOMATED HISTORY TRACKER FACTORY      
#auditor = audit_alembic.Auditor.create(APP_VERSION)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

#  ----- Audit Alembic
#def log_revision_creation(context, revision, directives):
#    """Este hook se ejecuta AUTOMÁTICAMENTE al usar 'alembic revision'"""
#    # Extraer los datos de la revisión que se está creando
#    script = directives[0]
#    rev_id = script.rev_id
#    message = script.message or "Sin mensaje"
#    created_at = datetime.datetime.now().isoformat()
#    
#    # Obtener la URL de la base de datos desde la configuración de Alembic
#    db_url = context.config.get_main_option("sqlalchemy.url")
#    engine = create_engine(db_url)
#    
#    with engine.begin() as connection:
#        # 1. Crear la tabla de logs si aún no existe en tu SQLite
#        connection.execute(text("""
#            CREATE TABLE IF NOT EXISTS alembic_revision_log (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                version_hash TEXT NOT NULL,
#                message TEXT,
#                created_at TEXT NOT NULL
#            );
#        """))
#        
#        # 2. Insertar el registro de la nueva migración creada
#        connection.execute(
#            text("""
#                INSERT INTO alembic_revision_log (version_hash, message, created_at)
#                VALUES (:version_hash, :message, :created_at);
#            """),
#            {"version_hash": rev_id, "message": message, "created_at": created_at}
#        )
#    print(f" LOGS: Revisión {rev_id} guardada con éxito en 'alembic_revision_log'")

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True
    )
    #  ----- Audit Alembic
    #"""on_version_apply=auditor.listen,"""

    #  Log revision:
    process_revision_directives=log_revision_creation 

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
            render_as_batch=True
        )

        #  Log revision:
        process_revision_directives=log_revision_creation 

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()