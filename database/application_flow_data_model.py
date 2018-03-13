from database.database_factory import DataBaseFactory


class ApplicationFlowDataModel:



    def loadDataIntoApplicationFlowTable(self, file_name, table_name):

        database_factory = DataBaseFactory()
        #cursor = database_factory.createConnection()
        database_factory.formLoadQuery(file_name,table_name)
        #database_factory.closeConnection()
        return


    #
    #
    #   TODO : Function is incomplete. Have to complete it
    #
    def ingestDataIntoApplicationFlowTable(self, application_data_array):

        for each in application_data_array:
            query = "INSERT INTO `natve`.`applicationflow_in` VALUES (%s,%s,%s)" % (each[0],"we", "ww")

        return



aa = ApplicationFlowDataModel()
aa.ingestDataIntoApplicationFlowTable("")