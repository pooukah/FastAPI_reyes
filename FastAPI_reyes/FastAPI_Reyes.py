from fastapi import FastAPI

app = FastAPI()

users = []

@app.post("/api/users", response_model=dict)
async def create_user(user_data: dict):

    users.append(user_data)
    return users