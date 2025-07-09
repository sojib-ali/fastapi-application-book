from fastapi import FastAPI, Depends, Query, HTTPException, status

app = FastAPI()

#the dependency function 
def user_dep(name: str = Query(..., min_length=3), password: str = Query(..., min_length=8)):
    """
    This dependency function would typically handle user validation or lookup.
    For this demo, it just confirms the user exists.
    """
    return {
        "name": name, "valid": True
    }

#web endpoint
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user


#define a user check dependency
def check_dep(name: str = Query(..., title="Username"), password: str = Query(..., title="Password")):
    """
    A dependency that only performs validation and doesn't return a value.
    If the validation fails, it raises a clear HTTP exception.
    """
    if name != "admin" or password != "secret":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials for check")

@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("demo_dependent:app", reload=True)