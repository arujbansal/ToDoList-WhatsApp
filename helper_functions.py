def info_in_db(cur, table_name):
    """
    Gets all the information from a table in the database.
    :param cur: The database cursor.
    :param table_name: The name of the table where you want to get the data from.
    :return: All the data in the table.
    """
    info = cur.execute(f"SELECT * FROM {table_name}")
    return [i for i in info]
