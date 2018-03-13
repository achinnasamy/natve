
import os

import pandas


class FileUtils:

    @staticmethod
    def readFile(file_name):
        with open(file_name, 'r') as file:
            content = file.read()

        return content


    #
    #
    # Specific to read applicationflow_in.txt file
    #
    @staticmethod
    def readTabSepApplicationFlowFile(filename):
        df = pandas.read_csv(filename, sep = "\t+|\s+\t+|\t+\s+", lineterminator='\r')
        return df

    #
    #
    #   Content can be list or string
    #
    #
    @staticmethod
    def writeToFile(file_name, content):
        row_string = ''
        with open(file_name, "w") as file:
            if(isinstance(content, (list,))):
                for each_row in content:
                    for each_element in each_row:
                        row_string = row_string + each_element + ","
                    file.write(row_string[:-1]+"\n")  # [:-1] remove the last , (comma) and write it to file
                    row_string = ''

                file.close()
            elif (isinstance(content, basestring)):
                file.write(content)
                file.close()
        return

    #
    # Delete the file
    #
    @staticmethod
    def delete_file(file_name):

        return