import asyncio
from datetime import datetime, timedelta

from faker import Faker
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import engine
from app.schemes import UserTrack
from app.models import Track
from app.utils import get_ip_info, get_user_agent


async def main():
    Faker.seed(0)

    fake = Faker()

    async with AsyncSession(engine) as session:
        for _ in range(1_000):
            user_agent = get_user_agent(fake.user_agent())
            ip_info = get_ip_info(fake.ipv4_public())

            track = UserTrack(
                url=fake.uri(),
                referrer=fake.uri(),
                screenWidth=fake.pyint(),
                screenHeight=fake.pyint(),
                isTouch=fake.pybool(),
                title=fake.sentence(),
                lang=fake.language_code(),
                userAgent=fake.user_agent(),
            )

            data = {
                **ip_info.dict(),
                **track.dict(),
                **dict(
                    user_agent=user_agent.user_agent.family,
                    os=user_agent.os.family,
                    device=user_agent.device.family,
                ),
            }

            db_track = Track(
                site="fake",
                timestamp=fake.date_time_between(
                    datetime.utcnow() - timedelta(weeks=4)
                ),
                **data,
            )

            session.add(db_track)
            await session.commit()


if __name__ == "__main__":
    asyncio.run(main())
