from fastapi import FastAPI


app = FastAPI(title='Advertising service')

@app.get('/')
def index():
    return {'Hello': 'World'}
