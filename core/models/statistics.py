from uuid import uuid4

from sqlalchemy import Column, Integer, Date, FLOAT
from sqlalchemy.dialects.postgresql import UUID

from core.database import Model


class Statistics(Model):
   __tablename__ = "statistics"

   id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
   date = Column(Date)
   views = Column(Integer)
   clicks = Column(Integer)
   cost = Column(FLOAT(precision=2))

