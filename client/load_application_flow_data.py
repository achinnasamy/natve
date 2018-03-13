
#
# Main file to run ApplicationDataFlow
# Load applicationflow_in.txt to `external`.`applicationflow_in` table
#
from database.application_flow_data_model import ApplicationFlowDataModel
from natve_utils.file_utils import FileUtils

# Read the tab seperated
df = FileUtils.readTabSepApplicationFlowFile("/home/dharshekthvel/Desktop/natve/NATVE ITP Project/conf/applicationflow_in.txt")

# Parse the file and put it in a array
application_data_array = []

for index,row in df.iterrows():
    application_data_array.append(
        [row['#sg'] , row['dg'] , str(row['sip']) , str(row['port']) , str(row['protocol']) , str(row['dip']) , str(
            row['mcastip']) , str(row['message'])])

# Write the array to temp file for bulk data load
FileUtils.writeToFile("/home/dharshekthvel/Desktop/natve/temp/temp_data_flow_file_for_mysql_load.csv",application_data_array)



# Load the data in the temp file to the mysql database
applicationDataFlowModel = ApplicationFlowDataModel()
applicationDataFlowModel.loadDataIntoApplicationFlowTable("/home/dharshekthvel/Desktop/natve/temp/temp_data_flow_file_for_mysql_load.csv",
                                                          "natve.applicationflow_in")
