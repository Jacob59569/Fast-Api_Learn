from fastapi import FastAPI, Query, Depends
import uvicorn
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class SHotel(BaseModel):
    adress: str
    name: str
    stars: int


class SHotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            stars: Optional[int] = Query(None, ge=1, le=5),
            has_spa: Optional[bool] = None
        ):
            self.location = location
            self.date_from = date_from
            self.date_to = date_to
            self.stars = stars
            self.has_spa = has_spa

@app.get('/hotels/')
def get_hotels(
        searchargs: SHotelsSearchArgs = Depends()
) -> list[SHotel]:
    hotels = [
        {
            'adress': 'Gagarina street',
            'name': 'Super Hotel',
            'stars': 5
        }
    ]

    return hotels

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/booking')
def add_booking(booking: SBooking):
    pass









if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)