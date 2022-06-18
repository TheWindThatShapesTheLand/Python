from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from web.db.villager import Villager
import pydantic

from web.db.functions.database import get_session
from web.models.functions import *


class VillagerService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_human(self, human_id: int):
        this_id = (self.session.query(Villager).filter_by(church_id=human_id).first())
        if not this_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return this_id

    def create(self, table_data: VillagerModel):
        new_table_data = Villager(**table_data.dict())  # распаковываем словарь в аргументы конструктора
        self.session.add(new_table_data)
        self.session.commit()
        return new_table_data

    def read(self, table_id):

        if table_id == "Villager":
            table_data = (self.session.query(Villager).all())
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return table_data

    def update(self, human_id: int, table_data: VillagerModel):
        villager = self._get_human(human_id)
        for field, value in table_data:
            setattr(villager, field, value)
        self.session.commit()
        return villager

    def delete(self, human_id: int):
        villager = self._get_human(human_id)
        self.session.delete(villager)
        self.session.commit()
