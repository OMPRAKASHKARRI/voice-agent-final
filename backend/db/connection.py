import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="voice_ai",
    user="postgres",
    password="admin123",   # your password
    port="5432"
)

conn.autocommit = True
cursor = conn.cursor()