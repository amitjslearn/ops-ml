from inference import Mnist
from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from io import BytesIO

app = FastAPI(title="MLOps Basics MNIST 3 or 7 App")
base_dir = Path('.')
model = Mnist(base_dir)

@app.get("/")
async def home():
    return "<h2>This is a sample NLP Project</h2>"


def read_imagefile(file):
    return (BytesIO(file))
    
@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg")
    if not extension:
        return "Image must be jpg or jpeg format!"
    image = read_imagefile(await file.read())
    prediction = model.infer(image)    
    return prediction

