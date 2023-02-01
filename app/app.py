from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlmodel.ext.asyncio.session import AsyncSession

from .database import init_db, get_session
from .models import Track
from .schemes import UserTrack
from .settings import settings
from .utils import get_ip_info, get_user_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=settings.static_dir), name="static")


@app.on_event("startup")
async def startup():
    await init_db()


@app.post("/tracks/{site}")
async def add_track(request: Request, site: str, track: UserTrack, session: AsyncSession = Depends(get_session)):
    user_agent = get_user_agent(track.user_agent)
    ip_info = get_ip_info(request.client.host)

    db_track = Track(
        site=site,
        **ip_info.dict(),
        **track.dict(),
        user_agent=user_agent.user_agent.family,
        os=user_agent.os.family,
        device=user_agent.device.family,
    )

    session.add(db_track)
    await session.commit()
