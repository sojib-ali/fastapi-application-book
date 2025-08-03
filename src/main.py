from fastapi import FastAPI
from .web import explorer,creature
from fastapi import File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from typing import Generator
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.include_router(explorer.router)
app.include_router(creature.router)

#to upload a small file

@app.post('/small')
async def upload_small_file(small_file: bytes = File()) -> str:
    return f'file size: {len(small_file)}'

#to upload a large file

@app.post('/big')
async def upload_big(big_file: UploadFile) -> str:
    return f'file size: {big_file.size}, name:{big_file.filename}'


#download small file

@app.get('/smile/{name}')
async def download_small_file(name):
    return FileResponse(name)

#download large file

def gen_file(path:str) -> Generator:
    with open(file=path, mode = 'rb') as file:
        yield file.read()

@app.get('/download_big/{name}')
async def donwload_big_file(name:str):
    gen_expr = gen_file(file_path=path)
    response = StreamingResponse(
        content = gen_expr,
        status_code = 200,
    )
    return response

#serving static files
#Make a directory called static, at the same level as main.py. (This can have any name; I’m calling it static only to help remember why I made it.)
#Put a text file called abc.txt in it, with the text contents abc :).

top = Path(__file__).resplve.parent

app.mount('/static',
          StaticFiles(directory = f'{top}/static', html = True),
          name = 'free')

# @app.get("/")
# def top():
#     return "top here"

# @app.get('/echo/{thing}')
# def echo(thing):
#     return f'echoing {thing}'

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run('main:app', reload = True)