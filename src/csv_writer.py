import os
import logging

def write_to_csv(dataframe, output_csv_file):
    """
    Write DataFrame to a CSV file.

    Parameters:
    - dataframe (pandas.DataFrame): DataFrame containing the data to be written.
    - output_csv_file (str): Path to the output CSV file.

    Returns:
    - None
    """
    output_dir = os.path.dirname(output_csv_file)
    os.makedirs(output_dir, exist_ok=True)

    if dataframe.empty:
        logging.info("No table found in PDF file. ")
    else:
        dataframe.to_csv(output_csv_file, index=False)
        logging.info(f"All tables merged and saved as {output_csv_file}")
