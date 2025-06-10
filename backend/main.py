from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/color")
async def get_random_color():
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#33FFF3"]
    return {"color": random.choice(colors)}

@app.get("/cat") 
async def get_random_cat_image():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.thecatapi.com/v1/images/search")
        if response.status_code == 200:
            data = response.json()
            image_url = data[0]['url']
            return {"cat_image_url": image_url}
        return JSONResponse(content={"error": "Failed to fetch cat image"}, status_code=500)

@app.get("/random-photo")
async def get_random_photo():
    width = random.randint(200, 600)
    height = random.randint(200, 600)
    photo_url = f"https://picsum.photos/{width}/{height}"
    return {"random_photo_url": photo_url}

@app.get("/time")
async def get_current_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": now}

@app.get("/scare")
async def scare():
    scare_images = [
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNm1jdjEyOGxtYnN4YWFyZDF3b3pjd29jZm44NTh1NHlxMThkbHNxZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FtlZhCjnGnKiA/giphy.gif",  
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2J6YjcyOXRlZXZ0eXl6ZjRnMTJtNXJ4emRmbWUyZ2psODBnZTZwMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiTnrRegEXN2AF0TS/giphy.gif"
    ]
    random_scare = random.choice(scare_images)
    return {"scare_image_url": random_scare}


@app.get("/lookalike")
async def lookalike():
    lookalike_images = [
        "https://randomuser.me/api/portraits/men/1.jpg",
        "https://randomuser.me/api/portraits/women/1.jpg",
        "https://randomuser.me/api/portraits/lego/1.jpg"
    ]
    random_lookalike = random.choice(lookalike_images)
    return {"lookalike_image_url": random_lookalike}
