from database.database_factory import DataBaseFactory
from natve_utils.file_utils import FileUtils


def create_all_tables():

    itp_message_bus_table = FileUtils.readFile("../ddl/itp_message_bus")
    print itp_message_bus_table

    dbf = DataBaseFactory()
    cursor = dbf.createConnection()
    dbf.executeQuery(cursor, itp_message_bus_table)




create_all_tables()