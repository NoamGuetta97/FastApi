from fastapi_chameleon import template
import fastapi

router = fastapi.APIRouter()


@router.get('/')
@template()
def index(user: str = 'anon'):
    return {
        'user_name': user
    }


@router.get('/about')
def about():
    return {}
