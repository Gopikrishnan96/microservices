from fastapi import FastAPI
from schema.schema import IrisData
from model.job import predict_iris

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "Iris Prediction API is up and running!"}

@app.post("/predict")
def predict(data: IrisData):
    input_data = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]
    prediction = predict_iris(input_data)
    return {"predicted_class": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)