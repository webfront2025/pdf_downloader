import unittest
import pandas as pd
import os

from app.services.excel_reader import ExcelReader


class TestExcelReader(unittest.TestCase):

    TEST_FILE = "test_excel.xlsx"

    def setUp(self):
        df = pd.DataFrame({
            "BRnum": ["TEST100"],
            "Pdf_URL": ["http://primary.com/file.pdf"],
            "Report Html Address": ["http://fallback.com/file.pdf"]
        })

        df.to_excel(self.TEST_FILE, index=False, engine="openpyxl")

    def tearDown(self):
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_excel_reading(self):
        reader = ExcelReader(self.TEST_FILE)
        reports = reader.read_reports()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0].br_number, "TEST100")
        self.assertEqual(reports[0].primary_url, "http://primary.com/file.pdf")