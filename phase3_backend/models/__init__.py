from models.base import Base, engine, get_db
from models.session import Session
from models.interaction import Interaction
from models.evaluation import Evaluation, ConfidenceHistory
from models.verification import VerificationAction

# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)
