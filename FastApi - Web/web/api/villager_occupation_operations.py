from typing import List, Optional
from fastapi import APIRouter, Response, Depends, status, HTTPException  # depends - внедрение зависимостей
import web.db.human
from web.models.functions import *
from web.db.functions.database import get_session
from web.db.human import Human
from web.services.villager_occupation_operations import VillagerOccupationService
from web.db.child import Child
from web.db.lord import Lord
from web.db.occupation import Occupation
from web.db.villager import Villager
from web.db.villager_occupation import VillagerOccupation
from web.user.models.usermodels import User


router = APIRouter(prefix='/operations')  # отчитываются не с начала, а от оператионс


@router.post('/villager occupation', tags=["Villager Occupation"])  # т.к. пост, то прочитать объект из тела запроса
def create(table_data: VillagerOccupationModel, service: VillagerOccupationService = Depends()):
    return service.create(table_data)


@router.get('/villager occupation', tags=["Villager Occupation"])  # что возвращяет
def read(table_id: str, service: VillagerOccupationService = Depends()):
    return service.read(table_id)


@router.put('/villager occupation', tags=["Villager Occupation"])
def update(table_id: int, table_data: VillagerOccupationModel, service: VillagerOccupationService = Depends()):
    return service.update(table_id, table_data)


@router.delete('/villager occupation', tags=["Villager Occupation"])
def delete(table_id: int, service: VillagerOccupationService = Depends()):
    service.delete(table_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
