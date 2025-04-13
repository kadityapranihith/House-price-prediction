from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

import util

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Or replace "*" with ["http://127.0.0.1:5500"] for security
    allow_credentials=True,
    allow_methods=["http://127.0.0.1:5500"],
    allow_headers=["http://127.0.0.1:5500"],
)
util.load_saved_artifacts()

@app.get("/get_location_names")
async def get_locations():
    return {"locations": util.get_locations()}

@app.post("/predict_home_price")
async def predict_home_price(
    total_sqft: float = Form(...),
    location: str = Form(...),
    bhk: int = Form(...),
    bath: int = Form(...)
):
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    return {"estimated_price": estimated_price}


if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI Server For Home Price Prediction...")
    util.load_saved_artifacts()
    uvicorn.run(app, host="0.0.0.0", port=8000)

