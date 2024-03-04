from fastapi import FastAPI
from routers import main_router

from application_1.routers.app_routers1 import router_app_1
from application_2.routers.app_routers2 import router_app_2
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(
    router=main_router,
    prefix='/check',
    tags=["Check"]
)
app.include_router(
    router=router_app_1,
    prefix='/start',
    tags=["App"]
)

app.include_router(
    router=router_app_2,
    prefix='/start',
    tags=["App"]
)

app.mount('/media', StaticFiles(directory='media'), name='media')