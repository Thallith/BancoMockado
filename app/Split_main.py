from fastapi import FastAPI
import uvicorn

app = FastAPI()


info = {
  'name': 'Thallith',
    'id': '22066',
    'Last_acess': '27/08/2022'
}

@app.get('/home')
def home():
    return 'Seja bem vindo ao meu Perfil acadêmico, <:'

@app.get('/about')
def about():
    return 'Sou estudante de Desenvolvimento de Sistemas e Linguagem de programação Python!!'

@app.get('/idade')
def get_users():
    return 15



@app.get('/')
def get_home():
    return info

if __name__ == '__main__':
    uvicorn.run(app=app, port=8080)