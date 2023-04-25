from fastapi import FastAPI, Body, status
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from game_database.db_connection import Database

# run: $ uvicorn main:app --reload

class ModelUserName(BaseModel):
    user_name: str

class ModelUserNameExperience(BaseModel):
    user_name: str
    experience: int

app = FastAPI()
db = Database()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(ValidationError)
async def handler1(request: Request, exc: Exception):
    print("ValidationError")
    print(type(exc))
    return JSONResponse(str(exc))


@app.exception_handler(RequestValidationError)
async def handler2(request: Request, exc: Exception):
    print("RequestValidationError")
    print(type(exc))
    return JSONResponse(str(exc))


@app.exception_handler(Exception)
async def handler3(request: Request, exc: Exception):
    print("Exception")
    print(type(exc))
    return JSONResponse(str(exc))

@app.get("/")
async def root():
    return {"status":"Im alive!!! 🚀"}

@app.post("/api/add/experience")
async def add_experience_api(item: ModelUserNameExperience):
    try:
        user_name = item.user_name
        print(f"add experience -- {user_name}")
        experience = item.experience
        request = db.add_experience(user_name, experience)
        retorno = {
            "status":request["status"],
            "message":request["message"]
        }
        print(f"ADD  EXPERIENCE --------- {retorno}")
        return JSONResponse(status_code=status.HTTP_200_OK, content=retorno)
    except Exception as e:
        return_item = {"status":"Error", "message":e}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=return_item)
    
@app.post("/api/get/experience")
async def get_experience_api(item: ModelUserName):
    try:
        user_name = item.user_name
        print(f"get experience -- {user_name}")
        experience = db.get_experience(user_name)["user_experience"]
        retorno = {
            "nome": user_name,
            "experience": str(experience),
            "message":""
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=retorno)
    except Exception as e:
        return_item = {"nome":item.user_name, "moedas":None, "message": "Este user não existe"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=return_item)
    
@app.post("/api/add/ranking")
async def add_ranking_api(item: ModelUserNameExperience):
    try:
        user_name = item.user_name
        print(f"add ranking -- {user_name}")
        new_experience = item.experience
        request = db.add_ranking(user_name, new_experience)
        retorno = {
            "status":request["status"],
            "message":request["message"]
        }
        print(f"ADD  ranking --------- {retorno}")
        return JSONResponse(status_code=status.HTTP_200_OK, content=retorno)
    except Exception as e:
        return_item = {"status":"Error", "message":e}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=return_item)

@app.get("/api/get/ranking")
async def get_ranking_api():
    try:
        ranking = db.get_ranking()["ranking"]
        retorno = {
            "ranking": ranking,
            "message":"Ranking atualizado",
            "player1_name": ranking[0]["player_name"],
            "player1_xp": ranking[0]["player_experience"],
            "player2_name": ranking[1]["player_name"],
            "player2_xp": ranking[1]["player_experience"],
            "player3_name": ranking[2]["player_name"],
            "player3_xp": ranking[2]["player_experience"],
            "player4_name": ranking[3]["player_name"],
            "player4_xp": ranking[3]["player_experience"],
            "player5_name": ranking[4]["player_name"],
            "player5_xp": ranking[4]["player_experience"],
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=retorno)
    except Exception as e:
        return_item = {"ranking":None, "message": "Erro"}
        print(e)
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=return_item)