from dataApi.databaseConnection import get_db
from dataApi.ormModel import User
from datetime import datetime
from sqlalchemy.orm import Session

async def create_user(db:Session
                    ,userName: str
                    ,loginTime: str 
                    ,logoutTime : str
                    ):
    query = User(User_Name=userName
                                 ,Login_Time = loginTime
                                ,Logout_Time = logoutTime)
    
    try:
        db.add(query)
        db.commit()
        return {"status": 200}
    except Exception as E:
        return {"status": 500}



