import shutil

from fastapi import APIRouter, File, UploadFile


router_app_1 = APIRouter()


@router_app_1.post('/application_1')
def response_application_1(file: UploadFile):
    path = f'application_1/files_app_1/{file.filename}'
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(file.file, buffer)
        return {f'file: {file.filename} saved!'}
