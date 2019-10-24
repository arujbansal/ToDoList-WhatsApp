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
    final_msg = []
    for k, v in commands_dict:
        final_msg.append(f'{k} - {v}')

    for i in range(len(final_msg)):
        final_msg[i] = f'{str(i)}. {final_msg[i]}'

    return ".\n".join(final_msg)
