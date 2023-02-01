from pydantic import BaseModel, Field, validator


class UserTrack(BaseModel):
    url: str
    referrer: str
    title: str
    lang: str
    user_agent: str = Field(alias="userAgent")
    screen_width: int = Field(alias="screenWidth")
    screen_height: int = Field(alias="screenHeight")
    is_touch: bool = Field(alias="isTouch")


class IPInfo(BaseModel):
    ip: str
    country_short: str | None
    country_long: str | None
    region: str | None
    city: str | None
    latitude: float
    longitude: float
    zipcode: str | None
    timezone: str | None

    @validator("*")
    def is_null(cls, v):
        return None if v == "-" else v


class Device(BaseModel):
    family: str
    major: str | None
    minor: str | None
    patch: str | None


class OS(BaseModel):
    family: str
    major: str | None
    minor: str | None
    patch: str | None
    patch_minor: str | None


class UserAgent(BaseModel):
    family: str
    major: str | None
    minor: str | None
    patch: str | None


class FullUserAgent(BaseModel):
    string: str
    device: Device
    user_agent: UserAgent
    os: OS
