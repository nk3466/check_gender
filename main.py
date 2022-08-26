from typing import List

from fastapi import FastAPI, File, UploadFile
import os

from model import model_pre

app = FastAPI()


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# STATIC_DIR = os.path.join(BASE_DIR,'static/')
# IMG_DIR = os.path.join(STATIC_DIR, 'static/images/')
# SERVER_IMG_DIR = os.path.join('http://localhost:8000/','static/', 'static/images/')

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/check_gender")
async def create_upload_files(files: List[UploadFile] = File(...)):
    UPLOAD_DIRECTORY = "static/images/"
    for file in files:
        contents = await file.read()
        with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
            fp.write(contents)

        result = model_pre(UPLOAD_DIRECTORY + file.filename)
    return {"result": result}
