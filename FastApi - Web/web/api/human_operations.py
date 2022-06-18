from typing import List, Optional
from fastapi import APIRouter, Response, Depends, status, HTTPException  # depends - внедрение зависимостей
import web.db.human
from web.models.functions import *
from web.db.functions.database import get_session
from web.db.human import Human
from web.services.human_operations import HumanService
from web.db.child import Child
from web.db.lord import Lord
from web.db.occupation import Occupation
from web.db.villager import Villager
from web.db.villager_occupation import VillagerOccupation
from web.user.models.usermodels import User


router = APIRouter(prefix='/operations')  # отчитываются не с начала, а от оператионс


@router.post('/human', tags=["Human"])  # т.к. пост, то прочитать объект из тела запроса
def create(table_data: HumanModel, service: HumanService = Depends()):
    return service.create(table_data)


@router.get('/human', tags=["Human"])  # что возвращяет
def read(table_id: str, service: HumanService = Depends()):
    return service.read(table_id)


@router.put('/human', tags=["Human"])
def update(table_id: int, table_data: HumanModel, service: HumanService = Depends()):
    return service.update(table_id, table_data)


@router.delete('/human', tags=["Human"])
def delete(table_id: int, service: HumanService = Depends()):
    service.delete(table_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
