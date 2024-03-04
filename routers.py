import shutil

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse, RedirectResponse

main_router = APIRouter()


@main_router.post("/chek_file")
def check_file(file: UploadFile = File()):
    content = file.file
    data = content.read()
    byte_list = [(bin(ch))[2:] for ch in data]
    byte_string = ''.join(byte_list)
    if byte_string.count('0') > byte_string.count('1'):
        return RedirectResponse('/start/application_1')
    else:
        return RedirectResponse('/start/application_2')