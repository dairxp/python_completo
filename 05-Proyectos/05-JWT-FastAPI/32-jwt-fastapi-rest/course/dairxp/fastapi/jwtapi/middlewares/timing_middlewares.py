import time
from fastapi import Request

async def timing_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f'{process_time:.4f}s'
    print(f'request.method: {request.url.path} -> response.status_code: {response.status_code}: {process_time:.4f}s')
    return response
