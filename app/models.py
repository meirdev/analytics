from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Field, SQLModel


class Track(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    site: str = Field(index=True)
    url: str
    referrer: str
    title: str
    lang: str = Field(index=True)
    screen_width: int
    screen_height: int
    is_touch: bool
    user_agent: str = Field(index=True)
    os: str = Field(index=True)
    device: str = Field(index=True)
    ip: str = Field(index=True)
    country_short: str | None = Field(index=True)
    country_long: str | None = Field(index=True)
    region: str | None
    city: str | None
    latitude: float
    longitude: float
    zipcode: str | None
    timezone: str | None
    timestamp: datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True), default=sa.func.now()))
