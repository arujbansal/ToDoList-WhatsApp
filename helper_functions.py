def info_in_db(cur, table_name):
    """
    Gets all the information from a table in the database.
    :param cur: The database cursor.
    :param table_name: The name of the table where you want to get the data from.
    :return: All the data in the table.
    """

    info = cur.execute(f"SELECT * FROM {table_name}")
    return [i for i in info]


def format_command_dict(commands_dict):
    """
    Formats the commands dictionary in a more readable manner.
    Adds a serial number to each command.
    Eg) 1. Help - Available commands.

    At the end of each command, there is '.\n'. This is used for displaying each command on the next line.
    :param commands_dict: The dictionary containing the commands.
    :return: A string ready to be sent to the user.
    """

    final_msg = ["Command - Usage"]
    for k, v in commands_dict.items():
        final_msg.append(f'{k} - {v}')

    for i in range(1, len(final_msg)):
        final_msg[i] = f'{str(i)}. {final_msg[i]}'

    return ".\n".join(final_msg)


def fetch_column_from_db(column_name, phone_number, table_name, cur):
    """
    Gets the information from a particular column in the database using a phone number.
    :param column_name: Name of column in database.
    :param phone_number: Phone number of user.
    :param table_name: The name of the table in the database.
    :param cur: Database cursor.
    :return: List of information.
    """

    cur.execute(f"SELECT {column_name} FROM {table_name} WHERE(Phone = '{phone_number}')")
    return cur.fetchone()


def update_column(column, table, phone_number, cursor, connection, new_info):
    """
    Updates a column in the database using a phone number.
    :param column: Column in the database.
    :param table: Table in the database.
    :param phone_number: Phone number of the user.
    :param cursor: Database cursor.
    :param connection: Database connection
    :param new_info: New information to be put in the column.
    """

    cursor.execute(f"UPDATE {table} SET {column} = '{new_info}' WHERE(Phone = '{phone_number}')")
    connection.commit()


def reformat_db_info(info):
    """
    Reformats database info into a proper list.
    :param info: QuerySet returned from database.
    :return: QuerySet converted to a list.
    """

    temp = ""
    for i in info:
        temp += i

    temp_list = temp.split(".\n")
    temp_list.pop()

    return [i + ".\n" for i in temp_list]


def add_numbering(info):
    """
    Adds a serial number to each task.
    :param info: The list of tasks.
    :return: String with proper numbering.
    """

    for i in range(len(info)):
        info[i] = f'{str(i + 1)}. {info[i]}'

    return ''.join(info)
