import sqlite3
from typing import List, Dict, Union, Tuple


class Database:
    """
    A class to interact with a SQLite database.

    Attributes:
    -----------
    db : sqlite3.Connection
        A connection to the SQLite database.
    """

    def __init__(self, db_name: str = "attendees.db") -> None:
        """
        Initializes a connection to the SQLite database.

        Parameters:
        -----------
        db_name : str, optional
            The name of the SQLite database to connect to. Defaults to "attendees.db".
        """
        self.db = sqlite3.connect(db_name)
        self.db.row_factory = sqlite3.Row
        print("DB connection initialized")

    def create_table(self, table_name: str, columns: List[str]) -> None:
        """
        Creates a new table in the database.

        Parameters:
        -----------
        table_name : str
            The name of the table to create.
        columns : List[str]
            A list of column names and their data types in the format "column_name data_type".
        """
        statement = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        self.db.execute(statement)
        self.db.commit()

    def read_one_row(self, statement: str, values: Union[Tuple, List]) -> Dict:
        """
        Executes a SELECT statement and returns the first row as a dictionary.

        Parameters:
        -----------
        statement : str
            The SELECT statement to execute.
        values : Tuple or List
            A tuple or list of values to substitute into the statement.

        Returns:
        --------
        Dict
            A dictionary representing the first row of the result set.
        """
        resource = self.db.execute(statement, values)
        row = resource.fetchone()
        if row is None:
            return None
        return dict(row)

    def read_all_rows(self, statement: str) -> List[Dict]:
        """
        Executes a SELECT statement and returns all rows as a list of dictionaries.

        Parameters:
        -----------
        statement : str
            The SELECT statement to execute.

        Returns:
        --------
        List[Dict]
            A list of dictionaries representing the result set.
        """
        resource = self.db.execute(statement)
        rows = resource.fetchall()
        return [dict(row) for row in rows]

    def change(self, statement: str, values: Union[Tuple, List]) -> int:
        """
        Executes an INSERT, UPDATE, or DELETE statement and returns the last row ID.

        Parameters:
        -----------
        statement : str
            The INSERT, UPDATE, or DELETE statement to execute.
        values : Tuple or List
            A tuple or list of values to substitute into the statement.

        Returns:
        --------
        int
            The last row ID of the affected rows.
        """
        result = self.db.execute(statement, values)
        self.db.commit()
        last_row_id = result.lastrowid
        if last_row_id is None:
            return 0
        return last_row_id

    def __del__(self) -> None:
        """
        Closes the connection to the SQLite database.
        """
        self.db.close()
        print("DB connection destroyed.")
