import shutil

from fastapi import APIRouter, File, UploadFile


router_app_2 = APIRouter()


@router_app_2.post('/application_2')
def response_application_2(file: UploadFile):
    path = f'application_2/files_app_2/{file.filename}'
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(file.file, buffer)
        return {f'file: {file.filename} saved!'}
