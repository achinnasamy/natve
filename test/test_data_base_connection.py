from database.database_factory import DataBaseFactory


database_factory = DataBaseFactory()
cursor = database_factory.createConnection()

print database_factory.ping(cursor)