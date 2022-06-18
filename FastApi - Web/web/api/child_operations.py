from typing import List, Optional
from fastapi import APIRouter, Response, Depends, status, HTTPException  # depends - внедрение зависимостей
import web.db.human
from web.models.functions import *
from web.db.functions.database import get_session
from web.db.human import Human
from web.services.child_operations import ChildService
from web.db.child import Child
from web.db.lord import Lord
from web.db.occupation import Occupation
from web.db.villager import Villager
from web.db.villager_occupation import VillagerOccupation
from web.user.models.usermodels import User


router = APIRouter(prefix='/operations')  # отчитываются не с начала, а от оператионс


@router.post('/child', tags=["Child"])  # т.к. пост, то прочитать объект из тела запроса
def create(table_data: ChildModel, service: ChildService = Depends()):
    return service.create(table_data)


@router.get('/child', tags=["Child"])  # что возвращяет
def read(table_id: str, service: ChildService = Depends()):
    return service.read(table_id)


@router.put('/child', tags=["Child"])
def update(table_id: int, table_data: ChildModel, service: ChildService = Depends()):
    return service.update(table_id, table_data)


@router.delete('/child', tags=["Child"])
def delete(table_id: int, service: ChildService = Depends()):
    service.delete(table_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
