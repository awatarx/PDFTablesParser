import unittest
import pandas as pd
from src.csv_writer import write_to_csv

class TestCSVWriter(unittest.TestCase):

    def test_write_to_csv(self):
        # Prepare test data
        data = {'Name': ['Awatar', 'raj', 'raju'],
                'Age': [25, 30, 35]}
        df = pd.DataFrame(data)
        
        # Define test output file
        test_output_csv_file = 'tests/test_output.csv'

        # Call the function
        write_to_csv(df, test_output_csv_file)

        # Read the written file and assert its content
        df_written = pd.read_csv(test_output_csv_file)
        self.assertTrue(df.equals(df_written))


