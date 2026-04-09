from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def read_root():
    return{"status: sucess","message: welcome to my first API !"}

@app.get("/name")
def get_name():
    return{"name:python developer","role:ai engineer"}