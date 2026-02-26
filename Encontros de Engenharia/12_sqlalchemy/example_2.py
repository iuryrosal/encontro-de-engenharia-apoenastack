from sqlalchemy import create_engine, text, select, Table, MetaData

engine = create_engine('sqlite:///database.db', echo=True)
metadata = MetaData()
users = Table('users', metadata, autoload_with=engine)
# with engine.connect() as con:
#     con.execute(text("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)"))
#     con.execute(text("INSERT INTO users (name) VALUES ('Alice')"))
#     con.execute(text("INSERT INTO users (name) VALUES ('Bob')"))
#     con.execute(text("INSERT INTO users (name) VALUES ('Iury')"))
#     con.commit()

with engine.connect() as con:
    # result = con.execute(text("SELECT * FROM users"))
    # print(result.fetchone())
    # print(result.fetchone())
    # print(result.fetchone())
    # print(result.fetchone())

    # print(result.fetchall())

    # print(result.fetchmany(2))

    select_users = select(users)
    iury_user = select_users.where(users.c.name == 'Iury')
    alice_user = select_users.where(users.c.name == 'Alice')

    result = con.execute(iury_user.limit(1))
    print(result.fetchall())
