from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def read_root():
    return{"Status": "Sucess","message": "Welcome to my first API !"}

@app.get("/name")
def get_name():
    return{"Name":"Python developer","Role": "Ai engineer"}