from fastapi import FastAPI

app = FastAPI(title = "BurgerBox API")

@app.get("/health")
async def health_check():
    return {"status": "grillin" , "version": "0.1.0"}

@app.get("/menu")
async def get_menu():
    return[
        {
            "name": "McAloo Tikki",
            "Price": 49,
            "is_vegetarian": True
        },
        {
            "name": "McEgg",
            "Price": 69,
            "is_vegetarian": False
        },
    ]