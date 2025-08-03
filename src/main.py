from fastapi import FastAPI
from .web import explorer,creature
from fastapi import File, UploadFile
from fastapi.responses import FileResponse

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

@app.get('/smile/{name}')
async def download_small_file(name):
    return FileResponse(name)



# @app.get("/")
# def top():
#     return "top here"

# @app.get('/echo/{thing}')
# def echo(thing):
#     return f'echoing {thing}'

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run('main:app', reload = True)