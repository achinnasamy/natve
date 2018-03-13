from database.database_factory import DataBaseFactory
from database.database_util import DataBaseUtilities
from natve_utils.log import Logger


#
#
#   Complete package for master control
#
#
#
class MasterConsole:



    #
    #
    #
    #
    #   The query to execute is UPDATE `itp`.`itp_message_bus` SET hash1 = '#6'; 
    #
    #
    def initialize_master_console(self):

        dbf = DataBaseFactory()
        cursor = dbf.createConnection()

        schema_table = DataBaseUtilities.concatenateSchemaTable("natve", "itp_message_bus")

        query = "UPDATE " + schema_table + " SET hash1 = '#6'"

        Logger.printLog(query)

        dbf.executeQuery(cursor, query)


        return

