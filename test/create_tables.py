from agent.db.database import engine
from agent.db.models import Base

Base.metadata.create_all(bind=engine)

print("Tables created")