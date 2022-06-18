import uvicorn
from fastapi import FastAPI
from settings import settings
from web.api.human_operations import router as human_router
from web.api.child_operations import router as child_router
from web.api.villager_operations import router as villager_router
from web.api.lord_operations import router as lord_router
from web.api.occupation_operations import router as occupation_router
from web.api.villager_occupation_operations import router as villager_occupation_router
from web.api.user_operations import router as user_occupation_router

app = FastAPI()
app.include_router(human_router)
app.include_router(child_router)
app.include_router(villager_router)
app.include_router(lord_router)
app.include_router(occupation_router)
app.include_router(villager_occupation_router)
app.include_router(user_occupation_router)

if __name__ == "__main__":
    uvicorn.run('main:app', port=settings.server_port, host=settings.server_host, reload=True)
