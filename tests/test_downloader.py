# ______________first test______________________
"""
from app.models.report import Report
from app.services.downloader import PDFDownloader
import unittest

class TestPDFDownloader(unittest.TestCase):

    def test_invalid_url(self):
        downloader = PDFDownloader("downloads")

        report = Report(
            br_number="TEST123",
            primary_url="http://invalid-url",
            fallback_url=None
        )

        result = downloader.download_reports([report])[0]  # download_reports returns a list

        self.assertEqual(result.status, "failed")
        self.assertEqual(result.file_path, None)
"""

import unittest
import os
import shutil

from app.models.report import Report
from app.services.downloader import PDFDownloader


class TestPDFDownloader(unittest.TestCase):

    TEST_FOLDER = "downloads_test"

    # Runs BEFORE each test
    def setUp(self):
        os.makedirs(self.TEST_FOLDER, exist_ok=True)
        self.downloader = PDFDownloader(
            output_directory=self.TEST_FOLDER,
            max_workers=1,
            timeout_seconds=5
        )

  
    # Runs AFTER each test    AND   Delete downloads_test folder in root of project
   
    def tearDown(self):
        if os.path.exists(self.TEST_FOLDER):
            shutil.rmtree(self.TEST_FOLDER)

 
    # Test 1: Invalid URL
  
    def test_invalid_url(self):
        report = Report(
            br_number="TEST001",
            primary_url="http://invalid-url",
            fallback_url=None
        )

        result = self.downloader.download_reports([report])[0]

        self.assertEqual(result.status, "failed")
        self.assertIsNone(result.file_path)

  
    # Test 2: Both URLs invalid

    def test_both_urls_invalid(self):
        report = Report(
            br_number="TEST002",
            primary_url="http://invalid-url",
            fallback_url="http://also-invalid"
        )

        result = self.downloader.download_reports([report])[0]

        self.assertEqual(result.status, "failed")
        self.assertIsNone(result.file_path)


    # Test 3: File already exists (skipped)
   
    def test_file_already_exists(self):
        file_path = os.path.join(self.TEST_FOLDER, "TEST003.pdf")

        # Create fake existing file
        with open(file_path, "w") as f:
            f.write("dummy content")

        report = Report(
            br_number="TEST003",
            primary_url="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
            fallback_url=None
        )

        result = self.downloader.download_reports([report])[0]

        self.assertEqual(result.status, "skipped")
        self.assertEqual(result.file_path, file_path)  