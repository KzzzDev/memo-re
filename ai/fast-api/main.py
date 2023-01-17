import uvicorn
import time
import functools
from script import api
from script import genimg 
from fastapi import FastAPI, status ,Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from queue import Queue

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


#queue
singleQueue=Queue(maxsize=1)
def multiple_control(q):
    def _multiple_control(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            q.put(time.time())
            print("/// [start] critial zone")
            result = func(*args,**kwargs)
            print("/// [end] critial zone")
            q.get()
            q.task_done()
            return result
        return wrapper
    return _multiple_control

class Ai(BaseModel):
    user_id: str
    keyword: str

class Api(BaseModel):
    file_name: str
    keyword: str

@app.post("/ai/",status_code = status.HTTP_201_CREATED)
@multiple_control(singleQueue)
def read_root(request: Api, response:Response):
    ai_response = api.generate(request.keyword,request.file_name)
    if ai_response != "error":
        #success
        response.status_code = status.HTTP_200_OK
        return
    else:
        #false
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return

@app.post("/ai/debug",status_code = status.HTTP_201_CREATED)
@multiple_control(singleQueue)
def read_root(request: Ai, response:Response):
    ai_response = genimg.generate(request.keyword,request.user_id)
    if ai_response != "error":
        #success
        response.status_code = status.HTTP_200_OK
        return {"img_file": ai_response}
    else:
        #false
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
