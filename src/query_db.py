import sqlite3
from src.generate_sql_query import generate_sql_query

def query_db(question):
    """ Query the SQLite database using the generated SQL query

    Args:
        question (str): Natural language question.

    Returns:
        results: Results of the query.
    """
    # Connect to SQLite database
    conn = sqlite3.connect("flights_database.db")
    cursor = conn.cursor()
    sql_query = generate_sql_query(question)
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()
        return sql_query, results
    except Exception as e:
        results = str(e)
        conn.close()
        return sql_query, results
