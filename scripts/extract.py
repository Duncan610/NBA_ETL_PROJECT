import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv
from datetime import datetime

# loading environment variables from the .env file
var = load_dotenv()

