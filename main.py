import datetime

from fastapi import FastAPI, Depends, HTTPException, status
from core.schemas.statistics import StatisticsDB, StatisticsOut
from core.repositories.statistics import StatisticsRepository
from core.database import Model, engine
from typing import List
from pydantic import parse_obj_as

Model.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/statistics/", response_model=StatisticsOut, status_code=status.HTTP_201_CREATED)
def create_statistics(statistics_instance: StatisticsDB, statistics: StatisticsRepository = Depends()):
    db_statistics = statistics.create(statistics_instance)

    return StatisticsOut.from_orm(db_statistics)


@app.get("/statistics", response_model=List[StatisticsOut])
def get_statistics(from_date: datetime.date, to_date: datetime.date, statistics: StatisticsRepository = Depends()):
    statistics_list = statistics.all(from_date, to_date)
    return parse_obj_as(List[StatisticsOut], statistics_list)


@app.post("/statistics/drop/", status_code=status.HTTP_200_OK)
def drop_statistics(statistics: StatisticsRepository = Depends()):
    statistics.remove_all()
