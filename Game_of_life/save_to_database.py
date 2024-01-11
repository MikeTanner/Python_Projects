import psycopg2

con = psycopg2.connect(
    host="localhost",
    port="5432",
    database="game_of_life",
    user="postgres",
    password="tanner12355",
)
# cursors are the vessel in which you communicate with the database
# open the cursor
cur = con.cursor()
# Query the data

cur.execute()
# cur.execute("insert into employees (id, name) values (1, "bob")")
# grab the data
con.close()
cur.close()
