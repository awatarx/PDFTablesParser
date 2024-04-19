import unittest
from src.pdf_parser import extract_tables_from_pdf

class TestPdfParser(unittest.TestCase):

    def test_extract_tables_from_pdf_valid_pdf(self):
        # Test for a valid PDF file
        pdf_path = "test_files/pdf1.pdf"
        result = extract_tables_from_pdf(pdf_path)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

    # TODO
    def test_extract_tables_from_pdf_empty_pdf(self):
        # Test for an empty PDF file
        pdf_path = "test_files/blank.pdf"
        result = extract_tables_from_pdf(pdf_path)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 0)

    # TODO 
    def test_extract_tables_from_pdf_no_tables(self):
        # Test for a PDF file with no tables
        pdf_path = "test_files/blank.pdf"
        result = extract_tables_from_pdf(pdf_path)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 0)

    def test_extract_tables_from_pdf_single_page_tables(self):
        # Test for a PDF file with single-page tables
        pdf_path = "test_files/pdf4.pdf"
        result = extract_tables_from_pdf(pdf_path)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

    def test_extract_tables_from_pdf_multi_page_tables(self):
        # Test for a PDF file with multi-page tables
        pdf_path = "test_files/pdf2.pdf"
        result = extract_tables_from_pdf(pdf_path)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

    def test_extract_tables_from_pdf_tables_in_different_formats(self):
        # Test for a PDF file with tables in different formats
        pdf_path = "test_files/pdf2.pdf"
        result = extract_tables_from_pdf(pdf_path)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

    # def test_extract_tables_from_pdf_rotated_tables(self):
    #     # Test for a PDF file with rotated tables
    #     pdf_path = "test_files/rotated_tables.pdf"
    #     result = extract_tables_from_pdf(pdf_path)
    #     self.assertIsNotNone(result)
    #     self.assertTrue(len(result) > 0)

    def test_extract_tables_from_pdf_encrypted_tables_no_password(self):
        # Test for a PDF file with encrypted tables (without providing a password)
        pdf_path = "test_files/pdf5.pdf"
        with self.assertRaises(Exception):
            extract_tables_from_pdf(pdf_path)

    def test_extract_tables_from_pdf_invalid_password(self):
        # Test for a PDF file with encrypted tables (providing an invalid password)
        pdf_path = "test_files/pdf5.pdf"
        password = "invalid_password"
        with self.assertRaises(Exception):
            extract_tables_from_pdf(pdf_path, password=password)

    def test_extract_tables_from_pdf_large_number_of_tables_pages(self):
        # Test for a PDF file with a large number of tables/pages
        pdf_path = "test_files/pdf3.pdf"
        result = extract_tables_from_pdf(pdf_path)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()



