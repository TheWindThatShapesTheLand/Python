from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from web.user.models.usermodels import User
import pydantic

from web.db.functions.database import get_session
from web.models.functions import *


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def reg(self, username: str, password: int, table_data: UserModel):
        this_id = (self.session.query(User).filter_by(name=username).first())
        if this_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        else:
            new_table_data = User(**table_data.dict())  # распаковываем словарь в аргументы конструктора
            self.session.add(new_table_data)
            self.session.commit()
            return new_table_data

    def auth(self):
        pass
