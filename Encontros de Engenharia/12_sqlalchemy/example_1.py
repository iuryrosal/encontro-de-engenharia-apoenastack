from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///database.db', echo=True)
print(engine)
print(engine.dialect)

# con = engine.connect()
# print(con.connection.dbapi_connection)

with engine.connect() as con:
    result = con.execute(text("SELECT 'Hello, World!'"))
    print(result.fetchone())
