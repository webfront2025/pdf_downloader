"""
            What is the purpose of this file?

                    This file is responsible only for reading the Excel file.

                    What happens inside it?

                    The Excel file is opened using pandas.

                    The required columns are validated (for example:

                                BRnum

                                Pdf_URL

                                Report Html Address

                    Each row is converted into a Report object.

                    A list of "Report" objects is returned.

                    Important:
                                This file does NOT perform any downloading.
                                It only converts raw Excel data into structured objects.
"""



import pandas as pd
from typing import List
from app.models.report import Report


class ExcelReader:

    REQUIRED_COLUMNS = ["BRnum", "Pdf_URL"]

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_reports(self) -> List[Report]:
        df = pd.read_excel(self.file_path, engine="openpyxl")
        print("Columns in Excel:", df.columns.tolist())

        self._validate_columns(df)
        reports = []

        has_fallback_column = "Report Html Address" in df.columns

        for _, row in df.iterrows():

            primary_url = row["Pdf_URL"]

            if pd.isna(primary_url):
                continue

            fallback_url = None

            if has_fallback_column:
                fallback_value = row["Report Html Address"]
                if not pd.isna(fallback_value):
                    fallback_url = fallback_value

            report = Report(
                br_number=str(row["BRnum"]),
                primary_url=primary_url,
                fallback_url=fallback_url
            )

            reports.append(report)

        return reports

    def _validate_columns(self, df):
        missing = [
            col for col in self.REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing:
            raise ValueError(f"Missing required columns: {missing}")