
import MySQLdb
from natve_utils.file_utils import FileUtils


class DataBaseFactory:

    db = None

    def createConnection(self):
        self.db = MySQLdb.connect("db4free.net", "natveuser", "natvepass", "natve")
        cursor = self.db.cursor()

        return cursor


    def closeConnection(self):
        self.db.close()
        return


    def ping(self, cursor):
        output = cursor.execute("SELECT VERSION()")
        return output


    def executeQuery(self, cursor, sql):
        cursor.execute(sql)
        return


    def fetchDB(self):

        return


    #
    #
    # For bulk loading of data, the below function is used to form the query
    #
    #
    def formLoadQuery(self, file_name, table_name):
        query = 'LOAD DATA INFILE \'%s\' INTO TABLE %s FIELDS TERMINATED BY \',\'' % (file_name, table_name)
        return query

