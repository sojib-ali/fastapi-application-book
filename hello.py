from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/hi")
def greet(who: str = Header("World", alias="X-Who")):
    return f"ola {who}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)