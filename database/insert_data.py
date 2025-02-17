import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("flights_database.db")

# Function to insert CSV data
def insert_csv(file, table):
    df = pd.read_csv(file)
    df.to_sql(table, conn, if_exists="append", index=False)

# Insert data
insert_csv("data/airlines.csv", "airlines")
insert_csv("data/airports.csv", "airports")
insert_csv("data/flights.csv", "flights")

# Commit and close
conn.commit()
conn.close()
