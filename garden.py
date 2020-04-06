""""mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="sammcfar21",
    password="greatnessisgreat",
    hostname="sammcfar21.mysql.pythonanywhere-services.com",
    databasename="sammcfar21$garden1"
    """

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="sammcfar21.mysql.pythonanywhere-services.com",
                                         database = 'sammcfar21$garden1',
                                         user = 'sammcfar21',
                                         password = "greatnessisgreat")
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error wile connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print ("MySQL connection is closed")

