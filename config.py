import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://fallback_url?sslmode=require")


