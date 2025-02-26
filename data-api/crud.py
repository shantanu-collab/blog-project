from databaseConnection import database
from ormModel import user
from datetime import datetime

async def create_user(userName: str
                    ,loginTime: str
                    ,logoutTime : str
                    ):
    query = user.insert().values(User_Name=userName
                                 ,Login_Time = loginTime
                                ,Logout_Time = logoutTime)
    return await database.execute(query)


