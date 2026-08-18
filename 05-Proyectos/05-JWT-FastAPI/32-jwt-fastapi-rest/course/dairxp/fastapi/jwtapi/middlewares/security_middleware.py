from fastapi import Request, status, HTTPException
from jose import jwt, JWTError
from starlette.responses import JSONResponse

from course.dairxp.fastapi.jwtapi.config.db import SessionLocal
from course.dairxp.fastapi.jwtapi.config.settings import settings
from course.dairxp.fastapi.jwtapi.respositories.sqlalchemy_user_repository import SQLAlchemyUserRepository

EXCLUDE_PREFIX = (
    '/docs',
    '/redoc',
    '/favicon.ico',
    '/openapi.json',
)
EXCLUDE_PATHS = [
    '/',
    '/oauth/token',
    '/oauth/token/form',
]
async def security_middleware(request: Request, call_next):
    path = request.url.path
    if path in EXCLUDE_PATHS or path.startswith(EXCLUDE_PREFIX):
        return await call_next(request)

    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={'detail': "Not authenticated"})

    token = auth.removeprefix('Bearer ') .strip()
    try:
        payload = jwt.decode(token,settings.JWT_SECRET,algorithms=[settings.JWT_ALGORITHM])
        user_id = int(payload.get('sub'))
    except (JWTError, TypeError, ValueError):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={'detail': "Token Invalido"})

    with SessionLocal() as db:
        user =SQLAlchemyUserRepository(db).find_by_id(user_id)
        if not user:
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={'detail': "Token Invalido"})

        request.state.user = user
    return await call_next(request)