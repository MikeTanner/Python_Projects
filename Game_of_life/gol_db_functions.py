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
# cur.execute("insert into employees (id, name) values (1, "bob")")
# grab the data


def save(game_board_data=[[[3]]], n=0, width=0, height=0):
    arr1 = [2]
    arr2 = [[3], [233]]
    cur.execute(
        """INSERT INTO "test" (gregtest, gregtest2)
          VALUES (%s, %s);""",
        (arr1, arr2),
    )
    cur.execute(
        """INSERT INTO "game_saves" (game_rounds, num_rounds, board_width, board_height)
          VALUES (%s, %s, %s, %s);""",
        (game_board_data, n, width, height),
    )
    close()
    # print(cur.fetchall())


def load(id=1):
    cur.execute(f"""Select * from game_saves where id = {id};""")
    rows = cur.fetchone()
    print(rows)
    return ()


def close():
    con.commit()
    con.close()
    cur.close()


load()
