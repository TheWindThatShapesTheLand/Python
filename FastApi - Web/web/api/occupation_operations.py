from typing import List, Optional
from fastapi import APIRouter, Response, Depends, status, HTTPException  # depends - внедрение зависимостей
import web.db.human
from web.models.functions import *
from web.db.functions.database import get_session
from web.db.human import Human
from web.services.occupation_operations import OccupationService
from web.db.child import Child
from web.db.lord import Lord
from web.db.occupation import Occupation
from web.db.villager import Villager
from web.db.villager_occupation import VillagerOccupation
from web.user.models.usermodels import User


router = APIRouter(prefix='/operations')  # отчитываются не с начала, а от оператионс


@router.post('/occupation', tags=["Occupation"])  # т.к. пост, то прочитать объект из тела запроса
def create(table_data: OccupationModel, service: OccupationService = Depends()):
    return service.create(table_data)


@router.get('/occupation', tags=["Occupation"])  # что возвращяет
def read(table_id: str, service: OccupationService = Depends()):
    return service.read(table_id)


@router.put('/occupation', tags=["Occupation"])
def update(table_id: str, table_data: OccupationModel, service: OccupationService = Depends()):
    return service.update(table_id, table_data)


@router.delete('/occupation', tags=["Occupation"])
def delete(table_id: str, service: OccupationService = Depends()):
    service.delete(table_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
