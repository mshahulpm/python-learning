from fastapi import FastAPI, BackgroundTasks
from event_manager import EventManager, EventManagerAsync

event_manager = EventManager()
event_manager_async = EventManagerAsync()
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the server"}


@app.get("/event-before")
def event_before():
    event_manager.high_compute()
    return {"message": "Event completed before sending the response"}


@app.get("/event-before-async")
def event_before_async():
    event_manager_async.run_high_compute_async()
    return {"message": "Event running before sending the response"}


@app.get("/event-after")
def event_after(bg_task: BackgroundTasks):
    bg_task.add_task(event_manager.high_compute)
    return {"message": "Event completed before sending the response"}
