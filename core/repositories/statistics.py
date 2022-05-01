from typing import List
from uuid import UUID

from fastapi.params import Depends, Query
from sqlalchemy.orm import Session

from ..models.statistics import Statistics
from ..dependencies import get_db
from ..schemas.statistics import StatisticsOut, StatisticsDB


class StatisticsRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find(self, uuid: UUID) -> Statistics:
        query = self.db.query(Statistics)
        return query.filter(Statistics.id == uuid).first()

    def all(self, from_date, to_date, sort_by) -> List[Statistics]:
        query = self.db.query(Statistics)
        # return query.all()
        return query.filter(Statistics.date >= from_date, Statistics.date <= to_date).all()

    def create(self, statistics: StatisticsDB) -> Statistics:
        db_statistics = Statistics(**statistics.dict())
        self.db.add(db_statistics)
        self.db.commit()
        self.db.refresh(db_statistics)  # TODO probably remove

        return db_statistics

    def remove_all(self):
        query = self.db.query(Statistics)
        query.delete()
        self.db.commit()
        # print(query)
        # print(query.delete())

