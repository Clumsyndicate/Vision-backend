import mysql.connector
from mysql.connector import Error
from flaskr.config import _MYSQL_DBNAME, _MYSQL_HOST, _MYSQL_USERNAME, _MYSQL_PASSWORD


def convert_to_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into images table")
    try:
        connection = mysql.connector.connect(host=_MYSQL_HOST,
                                             database=_MYSQL_DBNAME,
                                             user=_MYSQL_USERNAME,
                                             password=_MYSQL_PASSWORD)

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO Photos
                          (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

        tempPicture = convert_to_binary_data(photo)
        file = convert_to_binary_data(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, tempPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "Eric", "D:\Python\Articles\my_SQL\images\eric_photo.png",
           "D:\Python\Articles\my_SQL\images\eric_bioData.txt")
insertBLOB(2, "Scott", "D:\Python\Articles\my_SQL\images\scott_photo.png",
           "D:\Python\Articles\my_SQL\images\scott_bioData.txt")