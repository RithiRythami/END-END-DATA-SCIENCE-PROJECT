import uvicorn ##ASGI
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def index():
    return {'message': 'Hi,Everyone '}
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To my webpage': f'{name}'}

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000,reload=True)