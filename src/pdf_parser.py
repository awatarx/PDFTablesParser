import camelot
import pandas as pd

def extract_tables_from_pdf(pdf_path, password=None):
    """
    Extract tables from a PDF file using Camelot library.

    Parameters:
    - pdf_path (str): Path to the PDF file.
    - password (str, optional): Password for encrypted PDF files.

    Returns:
    - pandas.DataFrame: Concatenated DataFrame containing tables from the PDF.
    """

    if password:
        tables_lattice = camelot.read_pdf(pdf_path, flavor='lattice', pages='all', process_background=False, password=password)
    else:
        # process_background=False: This parameter is set to False to disable processing of background elements in the PDF. 
        # Works best if line border is hidden, but affects the normal table, so I set to False.
        tables_lattice = camelot.read_pdf(pdf_path, flavor='lattice', pages='all', process_background=False)
        

    if not tables_lattice:
        return pd.DataFrame()

    concatenated_df = pd.concat([table.df for table in tables_lattice])

    return concatenated_df
