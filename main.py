import fastapi
import uvicorn
import fastapi_chameleon
from starlette.staticfiles import StaticFiles

from views import home, account, packages

# fastapi
app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)


def configure():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    configure_templates()
    configure_routes()


def configure_templates():
    fastapi_chameleon.global_init('templates')


def configure_routes():
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:
    configure()
