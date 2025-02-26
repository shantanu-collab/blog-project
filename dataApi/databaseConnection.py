from sqlalchemy import create_engine, MetaData
import urllib
from sqlalchemy.orm import sessionmaker

# Database Configuration
DB_SERVER = "localhost"  # Change this to your actual SQL Server name
DB_NAME = "master"  # Change to your actual database name
DB_DRIVER = "ODBC Driver 17 for SQL Server"  # Ensure this is installed

# Encode driver name safely
DB_DRIVER_ENCODED = urllib.parse.quote_plus(DB_DRIVER)

# Correct DATABASE_URL for Synchronous Connection with pyodbc
DATABASE_URL = f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}?trusted_connection=yes&driver={DB_DRIVER_ENCODED}"

# For Sync Connection
engine = create_engine(DATABASE_URL, echo=True)  # echo=True for debugging queries
metadata = MetaData()

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
