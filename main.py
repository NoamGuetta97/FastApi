import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template


from views import home
from views import account
from views import packages

app = fastapi.FastAPI()

# chameleon:
fastapi_chameleon.global_init('templates')

app.include_router(home.router)
app.include_router(account.router)
app.include_router(packages.router)


if __name__ == '__main__':
    # no inspection PyTypeChecker
    uvicorn.run(app)
