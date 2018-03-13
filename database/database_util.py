
#
#   All methods in the class are static
#
#
#
class DataBaseUtilities:

    @staticmethod
    def concatenateSchemaTable(schema, table_name):
        return "`" + schema + "`" + "." + "`" + table_name + "`"


    @staticmethod
    def prepareUpdateQuery(self, schema_table_name, end_of_query):

        return 'UPDATE ' + schema_table_name + end_of_query