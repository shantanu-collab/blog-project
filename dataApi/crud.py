from dataApi.databaseConnection import get_db
from dataApi.ormModel import user
from datetime import datetime
from sqlalchemy.orm import Session

async def create_user(db:Session
                    ,userName: str
                    ,loginTime: str
                    ,logoutTime : str
                    ):
    query = user.insert().values(User_Name=userName
                                 ,Login_Time = loginTime
                                ,Logout_Time = logoutTime)
    return await db.execute(query)



