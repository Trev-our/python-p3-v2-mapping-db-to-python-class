
import pytest


class TestDepartment:
    '''Class Department in department.py'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''drop tables prior to each test.'''


    def test_creates_table(self):
        '''contains method "create_table()" that creates table "departments" if it does not exist.'''

        
    def test_drops_table(self):
        '''contains method "drop_table()" that drops table "departments" if it exists.'''

        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
     
        sql_table_names = """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='departments'
        """
       
        
    def test_saves_department(self):
        '''contains method "save()" that saves a Department instance to the db and assigns the instance an id.'''

      
        sql = """
            SELECT * FROM departments
        """
       
    def test_creates_department(self):
        '''contains method "create()" that creates a new row in the db using parameter data and returns a Department instance.'''

        sql = """
            SELECT * FROM departments
        """
       
    def test_updates_row(self):
        '''contains a method "update()" that updates an instance's corresponding db row to match its new attribute values.'''
      

       
       

        # Assign new values for name and location
       

        # Persist the updated name and location values
        
        # assert department1 row was not updated, department1 object state not updated
        # assert row not updated
       
        # assert department2 row was updated, department2 object state is correct
       
    def test_deletes_row(self):
        '''contains a method "delete()" that deletes the instance's corresponding db row'''
     
      
       

       
        # assert department1 row was not deleted, department1 object state is correct
        
        # assert department2 row is deleted
      
        # assert department2 object state is correct, id should be None
       
        # assert dictionary entry was deleted
       

    def test_instance_from_db(self):
        '''contains method "instance_from_db()" that takes a table row and returns a Department instance.'''

      

        sql = """
            SELECT * FROM departments
        """
        

        
        '''contains method "get_all()" that returns a list of Department instances for every row in the db.'''


    def test_finds_by_id(self):
        '''contains method "find_by_id()" that returns a Department instance corresponding to the db row retrieved by id.'''

     
