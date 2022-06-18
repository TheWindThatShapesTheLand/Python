from fastapi import APIRouter
from web.api.human_operations import router as human_operations_router
from web.api.child_operations import router as child_operations_router
from web.api.villager_operations import router as villager_operations_router
from web.api.lord_operations import router as lord_operations_router
from web.api.occupation_operations import router as occupation_operations_router
from web.api.villager_occupation_operations import router as villager_occupation_operations_router
from web.api.user_operations import router as user_operations_router

router = APIRouter()
router.include_router(human_operations_router)
router.include_router(child_operations_router)
router.include_router(villager_operations_router)
router.include_router(lord_operations_router)
router.include_router(occupation_operations_router)
router.include_router(villager_occupation_operations_router)
router.include_router(user_operations_router)
