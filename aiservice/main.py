from fastapi import FastAPI
import uvicorn
from routes import router as api_router

app = FastAPI()

# Подключение роутов
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)