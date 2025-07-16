

from fastapi import FastAPI, Header, Response

app = FastAPI()

@app.post("/hi")
def greet(who: str = Header("World", alias="X-Who")):
    return f"ola {who}"

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/header/{name}/{value}")
def set_response_header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)