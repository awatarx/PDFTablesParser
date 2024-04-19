import os
import logging
from utils import setup_logging
from csv_writer import write_to_csv
from pdf_parser import extract_tables_from_pdf
from pypdf.errors import FileNotDecryptedError, PdfStreamError

def extract_tables(pdf_file, output_csv_file, max_attempts=3):
    """
    Extract tables from a PDF file and write them to a CSV file.

    Parameters:
    - pdf_file (str): Path to the input PDF file.
    - output_csv_file (str): Path to the output CSV file.
    - max_attempts (int, optional): Maximum number of attempts for password input.

    Returns:
    - None
    """
    extracted_data = None
    
    # Attempt to extract tables from PDF
    try:
        extracted_data = extract_tables_from_pdf(pdf_file)
    except FileNotDecryptedError:
        extracted_data = try_decrypt_pdf(pdf_file, max_attempts=max_attempts)
    except PdfStreamError:
        logging.error("Looks like your PDF is corrupted. Try a valid PDF!")

    # Write extracted data to CSV file
    if extracted_data is not None:
        write_to_csv(extracted_data, output_csv_file)

def try_decrypt_pdf(pdf_file, max_attempts=3):
    """
    Attempt to decrypt an encrypted PDF file.

    Parameters:
    - pdf_file (str): Path to the input PDF file.
    - max_attempts (int, optional): Maximum number of attempts for password input.

    Returns:
    - pandas.DataFrame or None: Extracted tables from the PDF, or None if decryption failed.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            password = input("Please enter the password for the PDF file: ")
            extracted_data = extract_tables_from_pdf(pdf_file, password=password)
            return extracted_data
        except FileNotDecryptedError:
            if attempt < max_attempts:
                logging.error("Incorrect password. Please try again.")
            else:
                logging.error(f"Failed to decrypt PDF after {max_attempts} attempts. Exiting.")
                return None

def main():
    """
    Main function to extract tables from a PDF file and write them to a CSV file.
    """

    setup_logging()

    input_pdf_file_name = "pdf4.pdf"
    
    filename, extension = os.path.splitext(input_pdf_file_name)
    input_pdf_file = f"../test_files/{input_pdf_file_name}"
    output_csv_file = f"../csvs/{filename}.csv"

    # Extract tables from PDF and write to CSV
    extract_tables(input_pdf_file, output_csv_file)

if __name__ == "__main__":
    main()
