import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template
import fastapi_jinja


app = fastapi.FastAPI()

#chameleon:
fastapi_chameleon.global_init('templates')

#jinja:
#@fastapi_jinja.template(template_file='index.html')

@app.get('/')
@template(template_file='index.html')
def index(user: str = 'anon'):
    return {
        'user_name':user
    }

@app.get('/')
def about():
    return {}

@app.get('/account')
def index():
    return {}

@app.get('/account/register')
def register():
    return {}

@app.get('/account/login')
def login():
    return {}

@app.get('/account/logout')
def logout():
    return {}



if __name__ == '__main__':
    # noinspection PyTypeChecker
    uvicorn.run(app)
