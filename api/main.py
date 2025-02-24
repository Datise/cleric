from typing import Union
from fastapi import FastAPI
import rabbit
import json
app = FastAPI()

rabbit = rabbit.Rabbit()

@app.get("/")
def root():
    return {"Status": "Running"}


@app.post("/v1/agent/upload")
def agent_upload(data: dict):
    # print(f"DATA: {data['launch_files']}")
    files = json.dumps(data['launch_files'])
    rabbit.send_launch_files(files)
    return {"success": True}

@app.on_event("shutdown")
def shutdown_event():
    rabbit.channel.close()
    rabbit.connection.close()