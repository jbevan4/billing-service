from billing_service.domain.wallet.routes.wallet import router
from fastapi import FastAPI

app = FastAPI()


app.include_router(router)
