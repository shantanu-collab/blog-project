from sqlalchemy import create_engine, MetaData
from databases import Database
import urllib

# Database Configuration
DB_USERNAME = ""  # Change if needed
DB_PASSWORD = ""  # No password
DB_SERVER = "localhost"  # Change to your actual server name
DB_NAME = "master"  # Change to your actual database name
DB_DRIVER = "ODBC Driver 20 for SQL Server"

# Encode special characters safely
DB_DRIVER_ENCODED = urllib.parse.quote_plus(DB_DRIVER)

# Construct DATABASE_URL (No password)
DATABASE_URL = f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}?trusted_connection=yes&driver={DB_DRIVER_ENCODED}"

# For Async Connection
database = Database(DATABASE_URL)
metadata = MetaData()

# For Sync Connection
engine = create_engine(DATABASE_URL)
    

