from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline
import asyncio

text:str = "What is Text Summarization?"


app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        process = await asyncio.create_subprocess_exec("python", "main.py")
        await process.wait()
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predict_route(text: str):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e

def start():
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    start()
    
