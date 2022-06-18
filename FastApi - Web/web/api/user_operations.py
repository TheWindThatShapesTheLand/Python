from typing import List, Optional
from fastapi import APIRouter, Response, Depends, status, HTTPException  # depends - внедрение зависимостей
import web.db.human
from web.models.functions import *
from web.db.functions.database import get_session
from web.db.human import Human
from web.services.user_operations import UserService
from web.db.child import Child
from web.db.lord import Lord
from web.db.occupation import Occupation
from web.db.villager import Villager
from web.db.villager_occupation import VillagerOccupation
from web.user.models.usermodels import User


router = APIRouter(prefix='/operations')  # отчитываются не с начала, а от оператионс


@router.post('/user', tags=["User"])
def reg(username: str, password: int, table_data: UserModel, service: UserService = Depends()):
    return service.reg(username, password, table_data)


@router.get('/user', tags=["User"])
def auth(username: str, password: int, table_data: UserModel, service: UserService = Depends()):
    return service.reg(username, password, table_data)
