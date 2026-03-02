
"""
#************************************************** Export .csv file 
from typing import List
from app.models.download_result import DownloadResult

class ResultExporter:

    @staticmethod
    def export(results: List[DownloadResult], output_path: str):
        with open(output_path, "w", encoding="utf-8") as f:
            # Header
            f.write(", company , url , status , message , file_path ,\n")
            f.write(", ------- , --- , ------ , ------- , --------- ,\n")

            # Rows
            for r in results:
                url = r.primary_url or ""
                message = r.message or ""
                file_path = r.file_path or ""
                # br_number as company
                f.write(f", {r.br_number} , {url} , {r.status} , {message} , {file_path} ,\n")

# *************************************  Export to .xlsx file

import pandas as pd
from typing import List
from app.models.download_result import DownloadResult


class ResultExporter:

    def export(self, results: List[DownloadResult], output_file: str):

        data = []

        for result in results:
            data.append({
                "BR Number": result.br_number,
                "Primary URL": result.primary_url,
                "Fallback URL": result.fallback_url,
                "Status": result.status,
                "Message": result.message,
                "File Path": result.file_path
            })

        df = pd.DataFrame(data)

        # Write Excel file
        df.to_excel(output_file, index=False, engine="openpyxl")

        print(f"Results exported to {output_file}")
        """
        
        
        

from typing import List
from app.models.download_result import DownloadResult
import pandas as pd
import os

class ResultExporter:

    @staticmethod
    def export(results: List[DownloadResult], output_basename: str):
        """
        Export results to both CSV and Excel.
        :param results: List of DownloadResult
        :param output_basename: Path without extension, e.g., 'downloads/download_results'
        """
        # Ensure output folder exists
        os.makedirs(os.path.dirname(output_basename) or ".", exist_ok=True)

        # ---------------- Export CSV ----------------
        csv_file = f"{output_basename}.csv"
        with open(csv_file, "w", encoding="utf-8") as f:
            # Header
            f.write("company,url,status,message,file_path\n")
            # Rows
            for r in results:
                url = r.primary_url or ""
                message = r.message or ""
                file_path = r.file_path or ""
                f.write(f"{r.br_number},{url},{r.status},{message},{file_path}\n")

        print(f"Results exported to CSV: {csv_file}")

        # ---------------- Export Excel ----------------
        excel_file = f"{output_basename}.xlsx"
        data = []
        for r in results:
            data.append({
                "BR Number": r.br_number,
                "Primary URL": r.primary_url,
                "Fallback URL": r.fallback_url,
                "Status": r.status,
                "Message": r.message,
                "File Path": r.file_path
            })

        df = pd.DataFrame(data)
        df.to_excel(excel_file, index=False, engine="openpyxl")
        print(f"Results exported to Excel: {excel_file}")