from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from uzbeksongfinder import UzbekSongFinder

app = FastAPI()

@app.get("/", include_in_schema=False, response_class=HTMLResponse)
async def root():
    return "this is Uzbek Music Finder API, that can find uzbek songs. visit <a href='/docs'>/docs</a> page to see documentation<br><br>Bu Uzbek Song Finder API, Bu API o'zbekcha qo'shiqlar topib beradi dokumentatsiyani ko'rish uchun <a href='/docs'>/docs</a> pagega o'ting."

@app.get("/api/v1/search")
async def search(track: str):
    return UzbekSongFinder(track).search()