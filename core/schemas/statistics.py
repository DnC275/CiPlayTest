import datetime

from typing import Optional
from pydantic import BaseModel, root_validator, validator


class StatisticsDB(BaseModel):
    date: datetime.date
    views: int
    clicks: int
    cost: float

    class Config:
        orm_mode = True
        validate_assignment = True

    # @validator('cost', pre=True)
    # def validate_cost(cls, cost):
    #     return float('%.2f' % float(cost))


class StatisticsOut(StatisticsDB):
    cpc: Optional[float]
    cpm: Optional[float]

    @root_validator
    def set_cpc_cpm(cls, values):
        cpc = values['cost'] / values['clicks']
        cpm = values['cost'] / values['views'] * 1000

        values['cpc'] = float('%.2f' % cpc)
        values['cpm'] = float('%.2f' % cpm)

        return values

