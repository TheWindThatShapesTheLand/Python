from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from web.db.occupation import Occupation
import pydantic

from web.db.functions.database import get_session
from web.models.functions import *


class OccupationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_human(self, occupation_id: str):
        this_id = (self.session.query(Occupation).filter_by(profession=occupation_id).first())
        if not this_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return this_id

    def create(self, table_data: OccupationModel):
        new_table_data = Occupation(**table_data.dict())  # распаковываем словарь в аргументы конструктора
        self.session.add(new_table_data)
        self.session.commit()
        return new_table_data

    def read(self, table_id):

        if table_id == "Occupation":
            table_data = (self.session.query(Occupation).all())
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return table_data

    def update(self,  occupation_id: str, table_data: OccupationModel):
        occupation = self._get_human(occupation_id)
        for field, value in table_data:
            setattr(occupation, field, value)
        self.session.commit()
        return occupation

    def delete(self, occupation_id: str):
        occupation = self._get_human(occupation_id)
        self.session.delete(occupation)
        self.session.commit()
