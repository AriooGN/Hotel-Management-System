import cx_Oracle as orcl
from tkinter import messagebox
from utils import load_SQL_scripts
import logging

class OracleDBConnect:
    """
    This class represents a connection to an Oracle database.

    Args:
        username (str): The username for the database connection.
        password (str): The password for the database connection.
        host (str): The host name or IP address of the database server (default is 'oracle.scs.ryerson.ca').
        port (int): The port number for the database connection (default is 1521).
        sid (str): The SID (System Identifier) for the database (default is 'orcl').
    """
    def __init__(self, username: str, password: str, host: str = 'oracle.scs.ryerson.ca', port: int = 1521, sid: str = 'orcl'):
        """
        Initializes a new OracleDBConnect instance and establishes a database connection.

        Args:
            username (str): The username for the database connection.
            password (str): The password for the database connection.
            host (str): The host name or IP address of the database server (default is 'oracle.scs.ryerson.ca').
            port (int): The port number for the database connection (default is 1521).
            sid (str): The SID (System Identifier) for the database (default is 'orcl').
        """
        self.is_connected = False
        try:
            dsn = orcl.makedsn(host, port, sid=sid)
            self.connection = orcl.connect(username, password, dsn)
            self.cursor = self.connection.cursor()
            print('Connected to DB')
            self.is_connected = True
            self.final_create_table = load_SQL_scripts('lab9/SQL Commands/main operations/create_tables.sql')
            self.final_forced_drop = load_SQL_scripts('lab9/SQL Commands/main operations/drop_tables.sql')
            self.final_populate_tables = load_SQL_scripts('lab9/SQL Commands/main operations/populate.sql')
        except orcl.DatabaseError as e:
            self.errorMessage = str('Error', e)
            print(f'Failed to establish connection: {e}')

    def create_tables(self):
        """
        Executes SQL commands to create tables in the database.
        """
        self.execute_SQL_commands(self.final_create_table)
        
    def drop_tables(self):
        """
        Executes SQL commands to drop tables in the database.
        """
        self.execute_SQL_commands(self.final_forced_drop)

    def populate_tables(self):
        """
        Executes SQL commands to populate tables in the database.
        """
        self.execute_SQL_commands(self.final_populate_tables)

    def create_reservation(self, reservation_id, check_in_date, check_out_date):
        sql_command = """
        INSERT INTO Reservation (Reservation_ID, CheckInDate, CheckOutDate)
        VALUES (:reservation_id, TO_DATE(:check_in_date, 'YYYY-MM-DD'), TO_DATE(:check_out_date, 'YYYY-MM-DD'))
        """

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_command, {
                    'reservation_id': reservation_id,
                    'check_in_date': check_in_date,
                    'check_out_date': check_out_date
                })
                self.connection.commit()
                messagebox.showinfo("Successful", "Reservation created successfully")

        except orcl.DatabaseError as e:
            self.connection.rollback()
            messagebox.showerror("Error", f"An error occurred: {e}")

    def insert_room(self, room_number, bedsize, room_type, price=None):
        # SQL command for inserting into Room table
        room_sql = "INSERT INTO Room (RoomNumber, NumberOfBed, PricePerNight) VALUES (:RoomNumber, :NumberOfBed, :PricePerNight)"
        room_params = {'RoomNumber': room_number, 'NumberOfBed': 1 if bedsize else None, 'PricePerNight': price}

        # SQL command for inserting into specific room type table
        specific_room_sql = f"INSERT INTO {room_type}Room (RoomNumber, SizeOfBed) VALUES (:RoomNumber, :SizeOfBed)"
        specific_room_params = {'RoomNumber': room_number, 'SizeOfBed': bedsize}

        # Prepare the list of commands and their parameters
        sql_commands = [room_sql, specific_room_sql]
        command_params = [room_params, specific_room_params]

        # Execute the commands
        self.execute_SQL_commands(sql_commands, command_params)

    def passenger_query(self):
        command = load_SQL_scripts('lab9\SQL Commands\Queries\passenger.sql')
        return self.execute_SQL_commands(sql_commands=command, return_results=True)
    
    def personnel_query(self):
        command = load_SQL_scripts('lab9\SQL Commands\Queries\personnel.sql')
        return self.execute_SQL_commands(sql_commands=command,return_results=True)

    def reservation_query(self):
        command = load_SQL_scripts(r'lab9\SQL Commands\Queries\reservation.sql')
        return self.execute_SQL_commands(sql_commands=command,return_results=True)

    def room_query(self):
        command = load_SQL_scripts(r'lab9\SQL Commands\Queries\room.sql')
        return self.execute_SQL_commands(sql_commands=command,return_results=True)

    def payment_query(self):
        command = load_SQL_scripts('lab9\SQL Commands\Queries\payment.sql')
        return self.execute_SQL_commands(sql_commands=command,return_results=True)

    def execute_SQL_commands(self, sql_commands, command_params=None, return_results=False):
        """
        Executes a list of SQL commands using the existing database connection.

        :param sql_commands: List of SQL command strings.
        :param command_params: Optional list of dictionaries containing parameters for each command.
                               This list should be in the same order as the sql_commands.
        :param return_results: If set to True, the function will return the results of the queries.
        :return: List of results from each query if return_results is True; None otherwise.
        """
        if not isinstance(sql_commands, list):
            sql_commands = [sql_commands]

        print("command len: " + str(len(sql_commands)))
        results = []
        try:
            print(str(sql_commands) + '\n' + str(command_params))
            for idx, command in enumerate(sql_commands):
                print(str(idx) + ' asd ' + command)
                params = command_params[idx] if command_params and len(command_params) > idx else None

                if params is not None:
                    self.cursor.execute(command, params)

                else:
                    print(command)
                    self.cursor.execute(command)

                # Collect results if needed
                if return_results:
                    return (self.cursor.fetchall())
            self.connection.commit()
            if not return_results:
                messagebox.showinfo("Successful", "All commands executed successfully, changes committed.")
        except orcl.DatabaseError as e:
            self.connection.rollback()
            messagebox.showerror("Error", f"An error occurred: {e}\nRolling back... \nThe Following Command Failed\n{command}")
            return None

    def get_highest_Cid(self):
        command = """SELECT MAX(Customer_Id) FROM Passenger_ID"""
        return self.execute_SQL_commands(command,None,True)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print('Connection closed')

    
