from fastapi import FastAPI
from api.app.routers.default import router
from api.core.config import settings
import uvicorn

app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.APP_HOST, port=int(settings.APP_PORT))




